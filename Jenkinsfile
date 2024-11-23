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
              // Récupérer l'URL du service via Minikube
            def serviceURL = sh(script: "minikube service $RELEASE_NAME-service --url", returnStdout: true).trim()

            // Tester la connectivité à l'URL de santé (health check) de ton application
            sh "curl ${serviceURL}/health"
            }
        }
    }
}

    }
}
