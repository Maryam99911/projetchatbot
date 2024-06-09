from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Sélectionner la base de données
db = client['ProjetChatbot']

# Sélectionner la collection
collection = db["ConsommationElectriqueParJour"]

# Récupérer les documents de la collection
documents = collection.find()


def construire_contextes_consommation_electrique(data):
    contexts = []
    for entry in data:
        location = entry.get('location', 'localisation inconnue')
        batiments = ", ".join(
            [f"{key.replace('_', ' ').title()}: {value}" for key, value in entry.items() if key.startswith('batiment')])

        context = f"Le {location}, la consommation électrique par jour pour les bâtiments est : {batiments}."
        contexts.append(context)
    return contexts


# Construire les contextes à partir des documents récupérés
contexts_consommation_electrique = construire_contextes_consommation_electrique(documents)

# Afficher les contextes pour vérification
for context in contexts_consommation_electrique:
    print(context)
