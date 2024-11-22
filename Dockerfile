# image de base
FROM python:3.9-slim
# dossier de travail dans le conteneur
WORKDIR /app
# Copier le contenu du dossier courant 
COPY . /app
# Installer les dépendances requises
RUN pip install -r requirement.txt
# exposition du port 
EXPOSE 8000
# lancement du serveur flask 
CMD python3.9 app.py

