pipeline  {
    agent any

    environment {
        // Définir les variables d'environnement
        KUBECONFIG = '/home/ubuntu/.kube/config'  // Assurez-vous que ce fichier est accessible
        IMAGE_NAME = 'pedro1993/helloworld_img'   // Nom de l'image Docker
        DOCKER_CREDENTIALS = 'dockerhub-credentials' // Identifiants Docker Hub
    }

    stages {
        stage('Clone repository') {
            steps {
                script {

                    git clone 'https://github.com/BADRAAB/challenge.git'
                }
            }
        }

        stage('Build Docker image') {
            steps {
                script {
                    // Construire l'image Docker à partir du Dockerfile
                    sh "docker build  . -t $IMAGE_NAME:1.3 "
                }
            }
        }

        stage('Push image') {
            steps {
                script {
                    // Se connecter à Docker Hub et pousser l'image
                    withCredentials([usernamePassword(credentialsId: 'DOCKERHUB', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                        sh "docker login -u $USERNAME -p $PASSWORD"
                        sh "docker push $IMAGE_NAME"
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    // Appliquer les fichiers de déploiement Kubernetes et vérifier l'état des pods
                    sh '''
                    set -e
                    kubectl apply -f deployment.yaml
                    kubectl apply -f service.yaml
                    kubectl get pods
                    '''
                }
            }
        }
    }
}
