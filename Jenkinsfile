pipeline  {
    agent any

    environment {
        IMAGE_NAME = 'pedro1993/helloworld_img'  // Nom de l'image Docker
        DOCKER_CREDENTIALS = 'dockerhub-credentials' // Identifiants Docker Hub
        HELM_HOME = '/usr/local/bin/helm'  // Si Helm n'est pas dans le PATH
    }

    stages {
        stage('Clone repository') {
            steps {
                script {
<<<<<<< HEAD
=======

>>>>>>> 66dba6471212b912b068cbe73f77a6889c6f1e9a
                    git clone 'https://github.com/BADRAAB/challenge.git'
                }
            }
        }

        stage('Build Docker image') {
            steps {
                script {
<<<<<<< HEAD
                    sh "docker build -t $IMAGE_NAME:latest ."
=======
                    // Construire l'image Docker à partir du Dockerfile
                    sh "docker build  . -t $IMAGE_NAME:1.3 "
>>>>>>> 66dba6471212b912b068cbe73f77a6889c6f1e9a
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
                    // Initialiser Helm (si nécessaire)
                    sh 'helm repo update'

                    // Déployer l'application via Helm
                    sh "helm upgrade --install ${RELEASE_NAME} ./chart --set image.repository=${IMAGE_NAME} --set image.tag=latest"
                }
            }
        }
    }
}
