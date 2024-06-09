from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Sélectionner la base de données
db = client['ProjetChatbot']

# Sélectionner la collection
collection = db["candidatures-parcoursup2019"]

# Récupérer les documents de la collection
documents = collection.find()

# Fonction pour construire les contextes
def construire_contextes_candidatures_parcoursup(data):
    contexts = []
    for entry in data:
        filiere = entry.get('filiere', 'inconnu')
        nombre_candidatures = entry.get('nombre_candidatures', 'inconnu')

        context = f"La filière '{filiere}' a reçu {nombre_candidatures} candidatures."
        contexts.append(context)
    return contexts

# Construire les contextes à partir des documents récupérés
contexts_candidatures_parcoursup = construire_contextes_candidatures_parcoursup(documents)

# Afficher les contextes pour vérification
for context in contexts_candidatures_parcoursup:
    print(context)
