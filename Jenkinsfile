pipeline {
    agent any

    environment {
        KUBECONFIG = '/var/jenkins_home/.kube/config' // Chemin du kubeconfig dans le conteneur Jenkins
        IMAGE_NAME = 'pedro1993/helloworld_img' // Nom de l'image Docker
        RELEASE_NAME = 'helloworld' // Nom de la instance Helm
    }

    stages {
        stage('Clone repository') {
            steps {
                script {
                    git 'https://github.com/BADRAAB/challenge.git'
                }
            }
        }

        stage('Build Docker image') {
            steps {
                script {
                    // Construire l'image Docker à partir du Dockerfile
                    sh "docker build . -t $IMAGE_NAME:1.3"
                }
            }
        }

        stage('Push image') {
            steps {
                script {
                    // Se connecter à Docker Hub et pousser l'image
                    withCredentials([usernamePassword(credentialsId: 'DOCKERHUB', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                        sh "docker login -u $USERNAME -p $PASSWORD"
                        sh "docker push $IMAGE_NAME:1.3" // Utilisation de la version 1.3 ici
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    // Initialiser Helm (si nécessaire)
                    sh "helm version" // Cela peut être utile pour vérifier que Helm est bien installé

                    // Déployer l'application via Helm
                    sh "cd chart && helm install $RELEASE_NAME . -f values.yaml"
                }
            }
        }

        stage('Deploy test') {
            steps {
                script {
                    // Vérifier si le service est bien exposé
                    sh "kubectl get svc $RELEASE_NAME-service"

                    // Récupérer l'IP du LoadBalancer
                    def loadBalancerIP = sh(script: "kubectl get svc $RELEASE_NAME-service -o jsonpath='{.status.loadBalancer.ingress[0].ip}'", returnStdout: true).trim()

                    // Vérifier si une IP a été obtenue (attente si nécessaire)
                    while (!loadBalancerIP) {
                        echo "Attente de l'IP du LoadBalancer..."
                        sleep(10) // Attente de 10 secondes avant de réessayer
                        loadBalancerIP = sh(script: "kubectl get svc $RELEASE_NAME-service -o jsonpath='{.status.loadBalancer.ingress[0].ip}'", returnStdout: true).trim()
                    }

                    // Tester la connectivité à l'URL de santé (health check) de ton application
                    sh "curl http://${loadBalancerIP}:80/health"
                }
            }
        }
    }
}
