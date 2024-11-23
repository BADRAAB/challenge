**Environement**
	• Docker : pour builder l'image.
	• Minikube : pour créer un cluster Kubernetes .
	• Helm : pour la gestion des déploiements Kubernetes .
	• Jenkins : Pour la partie CI/CD (Jenkins  tourne dans un contneur docker)
	• Serveur Flask : S Framework python utilisé pour notre application .

**Structure de dossiers**
Challenge:
      chart:
         templates:
                 deployment.yaml 
                 service.yaml
                 ingress.yaml
         Chart.yaml
         values.yaml
     app.py
     Dockerfile
     Jenkinsfile
     requirement.txt
      

**Description des Composants**
1) Application Flask :
L'application Flask est une simple API avec deux routes :
	• / : Affiche un message "Hello World".
	• /health : Effectue un health check en retournant une réponse HTTP 200.
Ce fichier requirement  liste les dépendances Python nécessaires pour l'application Flask,

2) Dockerfile
Le Dockerfile permet de créer une image Docker de l'application Flask.
Il installe Python, copie l'application dans le conteneur, installe les dépendances, expose le port 8000, puis lance l'application Flask.

3)Fichiers Kubernetes 
Le déploiement de l'application : configure le déploiement de l'application (replica , image dans le dockerhub  ....) .
                                  pour la partie check health on peu configurer :
                                     -Temps d'attente avant de commencer à vérifier la santé  (initialDelaySeconds) 
                                     -Intervalle de temps entre chaque vérification (periodSeconds)
Le service Kubernetes : expose l'application via un service de type LoadBalancer, port container:8000  port-service:80

3)Fichier Helm 
	• Chart.yaml :  chart Helm (nom, version, description).
	• values.yaml : Contient les paramètres de configuration par défaut pour l'application, 
                  comme le nombre de réplicas, l'image Docker à utiliser, et les ports.

4) Pipeline Jenkins 
J'ai mis en place un Jenkinsfile contenant une pipeline CI/CD qui permet de :
	1. Cloner le dépôt.
	2. Construire l'image Docker.
	3. Pousser l'image vers Docker Hub.
	4. Déployer l'application sur Kubernetes via Helm.
	
**ETAPE DEPLOIEMENT**
Voici les étapes pour déployer l'application avec  Minikube et Jenkins :
	1.  Démarrez Minikube et configurez le kubeconfig dans jenkins  pour pouvoir interagir avec Kubernetes.
	2.  Mettre en place le webhook pour lier Jenkins à GITHUB et configuration du plugin github dans Jenkins.
	3. ajouter les credentials du dockerhub pour peremettre à Jenkis de faire le push de l'image. 
	4.  Lancer de la pipeline Jenkins en faisant un  commit au niveau de repot github . 







