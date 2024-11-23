# image de base
FROM python:3.9-slim
# dossier de travail dans le conteneur
WORKDIR /app
# Copier le contenu du dossier courant dans le contneur 
COPY . /app
# Installer les dépendances 
RUN pip install -r requirement.txt
# exposition du port 
EXPOSE 8000
# lancement du serveur flask 
CMD python3.9 app.py

