from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Sélectionner la base de données
db = client['ProjetChatbot']

# Sélectionner la collection
collection = db["ProjetsCVEC"]

# Récupérer les documents de la collection
documents = collection.find()

# Fonction pour construire les contextes
def construire_contextes_projets_cvec(data):
    contexts = []
    for entry in data:
        thematique = entry.get('thematique', 'inconnu')
        date = entry.get('date', 'inconnu')
        nom = entry.get('nom', 'inconnu')
        objectifs = entry.get('objectifs', 'inconnu')
        localisation = entry.get('localisation', 'inconnu')

        context = (f"Le projet '{nom}' de thématique '{thematique}' a été initié le {date}. "
                   f"Ses objectifs sont : {objectifs}. ")
        if localisation:
            context += f"Il se situe à l'adresse : {localisation}."
        else:
            context += "La localisation n'est pas spécifiée pour le moment."
        contexts.append(context)
    return contexts

# Construire les contextes à partir des documents récupérés
contexts_projets_cvec = construire_contextes_projets_cvec(documents)

# Afficher les contextes pour vérification
for context in contexts_projets_cvec:
    print(context)
