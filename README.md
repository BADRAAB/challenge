# Déploiement d'une Application Flask avec Docker, Kubernetes, Helm et Jenkins

## Environnement

- **Docker** : Utilisé pour construire l'image Docker.
- **Minikube** : Utilisé pour créer un cluster Kubernetes local.
- **Helm** : Outil de gestion des déploiements Kubernetes.
- **Jenkins** : Outil d'intégration continue et de déploiement continu (CI/CD), exécuté dans un conteneur Docker.
- **Flask** : Framework Python utilisé pour développer notre application.


## Structure des Dossiers

```
Challenge/
├── chart/
│   ├── templates/
│   │   ├── deployment.yaml
│   │   ├── service.yaml
│   │   ├── ingress.yaml
│   ├── Chart.yaml
│   ├── values.yaml
├── app.py
├── Dockerfile
├── Jenkinsfile
└── requirements.txt
```

## Description des Composants

### 1) Application Flask
L'application Flask est une simple API avec deux routes :
- `/` : Affiche un message "Hello World".
- `/health` : Effectue un health check en retournant une réponse HTTP 200.

Le fichier requirements.txt liste les dépendances Python nécessaires pour l'application Flask.

### 2) Dockerfile
Le `Dockerfile permet de créer une image Docker de l'application Flask. Voici les étapes qu'il suit :
1. Installe Python.
2. Copie l'application dans le conteneur.
3. Installe les dépendances Python à partir du fichier requirements.txt.
4. Expose le port 8000.
5. Lance l'application Flask.

### 3) Fichiers Kubernetes
#### Déploiement de l'application
Le fichier de deployment.yaml configure :
- Le nombre de réplicas.
- L'image Docker à utiliser depuis Docker Hub.
- Le health check :
  - **initialDelaySeconds** : Temps d'attente avant de commencer à vérifier la santé.
  - **periodSeconds** : Intervalle entre chaque vérification de la santé.

#### Service Kubernetes
Le fichier service.yaml expose l'application via un service de type LoadBalancer avec :
- Port conteneur : 8000
- Port du service : 80

### 4) Fichiers Helm
- **Chart.yaml** : Contient les métadonnées de notre chart Helm (nom, version, description).
- **values.yaml** : Contient les paramètres de configuration par défaut pour l'application, comme le nombre de réplicas, l'image Docker à utiliser, et les ports qui seront appliquées dans le deployment et le service.

### 5) Pipeline Jenkins
Le fichier Jenkinsfile définit une pipeline CI/CD qui permet de :
1. Cloner le dépôt.
2. Construire l'image Docker.
3. Pousser l'image vers Docker Hub.
4. Déployer l'application sur Kubernetes via Helm.

## Étapes de Déploiement

Voici les étapes pour déployer l'application avec Minikube et Jenkins :

### 1. Démarrer Minikube
- Lancez Minikube et configurez le kubeconfig dans Jenkins afin de pouvoir interagir avec votre cluster Kubernetes.

### 2. Configurer le Webhook pour GitHub
- Liez Jenkins à votre dépôt GitHub via un Webhook.
- Installez et configurez le plugin GitHub dans Jenkins.

### 3. Ajouter les Credentials Docker Hub
- Ajoutez les credentials Docker Hub dans Jenkins afin qu'il puisse pousser l'image vers Docker Hub.

### 4. Lancer la Pipeline Jenkins
- Faites un commit dans votre dépôt GitHub pour déclencher automatiquement la pipeline Jenkins.

La pipeline effectuera les étapes suivantes :
1. **Clonage du dépôt** : Récupère le code source.
2. **Build Docker** : Crée l'image Docker de l'application.
3. **Push Docker Image** : Pousse l'image Docker sur Docker Hub.
4. **Déploiement Kubernetes** : Utilise Helm pour déployer l'application sur Kubernetes.

---
