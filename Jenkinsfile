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
                    //clone du repo 
                    git 'https://github.com/BADRAAB/challenge.git'
                }
            }
        }

        stage('Build image') {
            steps {
                script {
                    //build de l'image docker
                    sh "docker build . -t $IMAGE_NAME:1.2"
                }
            }
        }

        stage('Push image') {
            steps {
                script {
                    //acceder à Dockerhub en utilisant les credential mis dans Jenkins puis push l'image
                    withCredentials([usernamePassword(credentialsId: 'DOCKERHUB', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                        sh "docker login -u $USERNAME -p $PASSWORD"
                        sh "docker push $IMAGE_NAME:1.3" 
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                   

                    // Déployer l'application via Helm dans le cluster  kubernetes
                  sh "cd chart && helm upgrade --install  $RELEASE_NAME . -f values.yaml"
                }
            }
        }

  

    }
}
