from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Sélectionner la base de données
db = client['ProjetChatbot']

# Sélectionner la collection
collection = db["BâtimentsetServicesdel'Universitéd'Evry"]


# Récupérer les documents de la collection
documents = collection.find()


# Fonction pour construire les contextes
def construire_contextes_batiments_services(data):
    contexts = []
    for entry in data:
        adresse = entry['adresse'] if entry['adresse'] is not None else 'adresse inconnue'
        code_postal = entry['code_postal'] if entry['code_postal'] is not None else 'code postal inconnu'
        commune = entry['commune'] if entry['commune'] is not None else 'commune inconnue'
        latitude = entry['latitude'] if entry['latitude'] is not None else 'latitude inconnue'
        longitude = entry['longitude'] if entry['longitude'] is not None else 'longitude inconnue'

        context = (f"Le {entry['type_de_donnee']} {entry['nom']} situé à {adresse} "
                   f"dans le code postal {code_postal} à {commune}, "
                   f"est localisé aux coordonnées ({latitude}, {longitude}).")
        contexts.append(context)
    return contexts


# Construire les contextes à partir des documents récupérés
contexts_batiments_services = construire_contextes_batiments_services(documents)

# Afficher les contextes pour vérification
for context in contexts_batiments_services:
    print(context)
