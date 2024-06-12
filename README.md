# Projet Chatbot Sacl-AI

# Description
Ce chatbot est conçu pour engager des conversations avec les utilisateurs et fournir des réponses basées sur des motifs et des intentions prédéfinis. Il utilise un modèle de réseau neuronal entraîné sur un ensemble de données d'intentions pour comprendre les entrées utilisateur et générer des réponses appropriées.

# Prérequis
Avant d'exécuter le chatbot, assurez-vous d'avoir installé les dépendances suivantes :
- Python 3.10
- NLTK (Natural Language Toolkit)
- TensorFlow
- NumPy
- MongoDB (le stockage de la dataset qu'on passe au modèle IA)

Vous pouvez installer ces dépendances en utilisant pip :
```
pip install nltk tensorflow numpy pymongo
```

# Utilisation
1. **Préparation des données** : Les données de conversation au format JSON sont construites en prenant les fichiers JSON contenant les données brutes en entrée et en les utilisant pour construire des contextes pertinents. Ces contextes ont été  ensuite organisés sous un format structuré de questions et réponses. Le fichier JSON résultant contient une liste d'intentions, où chaque intention se compose de motifs patterns (entrées utilisateur) et de réponses correspondantes.

2. **Entraînement** : Exécutez le script pour prétraiter les données, entraîner le modèle de réseau neuronal et enregistrer le modèle entraîné (`chatbot_model.h5`) ainsi que les métadonnées nécessaires (`data.pickle`).

3. **Conversation** : Lancez le script pour démarrer le chatbot. Commencez à interagir avec le bot en saisissant vos messages. Tapez 'quit' pour quitter la conversation.

#### Fichiers
- `data1.json` : Fichier JSON contenant les données de conversation (intentions et réponses).
- `chatbot_model.h5` : Modèle de réseau neuronal entraîné pour la classification des intentions.
- `data.pickle` : Fichier picklé contenant les données prétraitées (mots, libellés, données d'entraînement, données de sortie). Il est généré automatiquement après exécution du modèle.
- `main2.py` : L'implémentation du modèle.

#### Architecture du Modèle
L'architecture du modèle de chatbot se compose d'un réseau neuronal à propagation avant avec trois couches denses. La couche d'entrée prend la représentation bag-of-words de l'entrée utilisateur, et les couches suivantes consistent en des couches denses (entièrement connectées) avec des fonctions d'activation ReLU. La couche de sortie utilise une activation softmax pour la classification multi-classes.

#### Fonctionnement du Chatbot
- Lors de la réception de l'entrée utilisateur, le chatbot tokenize l'entrée, la convertit en une représentation bag-of-words, et la passe à travers le modèle entraîné.
- Le modèle prédit l'intention de l'entrée utilisateur, et en fonction du niveau de confiance de la prédiction, sélectionne une réponse appropriée parmi les réponses prédéfinies associées à cette intention.
- Si le niveau de confiance est en dessous d'un certain seuil, le chatbot invite l'utilisateur à réessayer ou fournit une réponse générique indiquant un manque de compréhension.

#### Remarques
Après un entrainement avec 1000 epochs et une taille de lot de 5. Le modèle affiche les performances suivantes :

- Exactitude (accuracy) : Le modèle a atteint une précision de 93,43 % (accuracy : 0.9343) sur les données d'entraînement, indiquant qu'il prédit correctement l'intention de l'utilisateur dans une grande proportion des cas.

- Perte (loss) : La valeur de perte (loss) obtenue est de 9.6239e-04, ce qui indique une faible erreur moyenne entre les prédictions du modèle et les valeurs réelles.

# Spécifcations sur la construction du fichier JSON d'entraînement
- Construction des contextes de questions et de réponses : Les fonctions construire_contextes_[....]_questions et construire_contextes_[....]_reponses transforment les documents MongoDB en contextes textuels.
- Génération de questions et réponses : On utilise des modèles de la bibliothèque transformers pour générer des questions et réponses à partir des contextes.

  
    **pipe_question** = pipeline("text2text-generation", model="lincoln/barthez-squadFR-fquad-piaf-question-generation")
    **qa_pipeline** = pipeline("question-answering", model="TARUNBHATT/flan-t5-small-finetuned-squad")
- Cryptage et Sauvegarde dans MongoDB : Après génération d'une paire de clés RSA, on les utilise pour crypter le jeu de données en utilisant AES et la clé AES qui est chiffrée avec RSA, puis stocker les données cryptées avec la clé de cryptage et le vecteur d'initialisation (IV) dans une collection MongoDB qu'on utilisera à chaque fois qu'on souhaite entraîner notre modèle. Cela assure que les informations sensibles sont stockées en toute sécurité et ne peuvent être accessibles que par quelqu'un possédant la clé de déchiffrement correcte.

# Déchiffrement des Données 
- Connexion à MongoDB : Le script se connecte à MongoDB pour récupérer les données chiffrées à partir de la collection chiffrée.
- Chargement de la Clé Privée : On charge la clé privée à partir d'un fichier PEM.
- Déchiffrement des Données : La fcontion decrypt permet de déchiffrer les données. Elle utilise la clé privée pour déchiffrer la clé AES et l'IV, puis utilise ces informations pour déchiffrer les données JSON.
- Utilisation des Données pour l'Entraînement du Modèle de Chatbot.
