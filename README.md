# Déploiement API Helloword sur Kubernetes

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
L'application Flask est une  API avec deux routes :
- `/` : Affiche un message "Hello World".
- `/health` : Effectue un health check en retournant une réponse HTTP 200.

Le fichier requirements.txt liste les dépendances Python nécessaires pour l'application Flask.

### 2) Dockerfile
1. Install Python.
2. Copie l'application dans le conteneur.
3. Install les dépendances à partir du fichier requirements.txt.
4. Expose le port 8000.
5. Lance l'application Flask.

### 3) Fichiers Kubernetes
#### Déploiement de l'application
Le fichier de deployment.yaml configure :
- Le nombre de réplicas.
- L'image Docker à utiliser depuis Docker Hub.
- Le health check ou on peut configurer :
  - **initialDelaySeconds** : Temps d'attente avant de commencer à vérifier la santé.
  - **periodSeconds** : Intervalle entre chaque vérification de la santé.

#### Service Kubernetes
Le fichier service.yaml expose l'application via un service de type LoadBalancer avec :
- Port conteneur : 8000
- Port du service : 80

### 4) Fichiers Helm
- **Chart.yaml** : données de notre chart Helm (nom, version, description).
- **values.yaml** : paramètres de configuration par défaut pour l'application, comme le nombre de réplicas, l'image Docker à utiliser, et les ports (qui seront appliquées au deployment au service).

### 5) Pipeline Jenkins
Le fichier Jenkinsfile définit une pipeline CI/CD qui permet de :
1. Cloner le dépôt.
2. Construire l'image Docker.
3. Pousser l'image vers Docker Hub.
4. Déployer l'application sur Kubernetes via Helm.

## Étapes de Déploiement

### 1. Démarrer Minikube
- Lancer Minikube et configurez le kubeconfig dans Jenkins afin de pouvoir interagir le cluster Kubernetes.

### 2. Configurer le Webhook pour GitHub
- Lier Jenkins au dépôt GitHub via un Webhook.
- Installer et configurez le plugin GitHub dans Jenkins.

### 3. Ajouter les Credentials Docker Hub
- Ajouter les credentials DockerHub dans Jenkins.

### 4. Lancer la Pipeline Jenkins
- Faire un push dans le dépôt GitHub pour déclencher automatiquement la pipeline Jenkins.

---
