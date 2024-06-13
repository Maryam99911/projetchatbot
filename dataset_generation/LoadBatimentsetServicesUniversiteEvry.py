from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Sélectionner la base de données
db = client['ProjetChatbot']

# Sélectionner la collection
collection = db["BâtimentsetServicesdel'Universitéd'Evry"]


# Récupérer les documents de la collection
documents = collection.find()
documents2 = collection.find()



# Fonction pour construire les contextes
def construire_contextes_batiments_services_questions(data):
    contexts = []
    for entry in data:
        adresse = entry['adresse'] if entry['adresse'] is not None else 'adresse inconnue'
        code_postal = entry['code_postal'] if entry['code_postal'] is not None else 'code postal inconnu'
        commune = entry['commune'] if entry['commune'] is not None else 'commune inconnue'
        latitude = entry['latitude'] if entry['latitude'] is not None else 'latitude inconnue'
        longitude = entry['longitude'] if entry['longitude'] is not None else 'longitude inconnue'
        adresse_complet = f" {adresse } {code_postal} {commune} {latitude} {longitude}"
        type_service = entry['type_de_donnee']
        nom = entry['nom']

        context = f"le {type_service} {nom.lower()} a pour <hl> Adresse <hl>s :  {adresse_complet.lower()} "

        contexts.append(nom)

    return contexts


def construire_contextes_batiments_services_reponses(data):
    contexts = []
    for entry in data:
        adresse = entry['adresse'] if entry['adresse'] is not None else 'adresse inconnue'
        code_postal = entry['code_postal'] if entry['code_postal'] is not None else 'code postal inconnu'
        commune = entry['commune'] if entry['commune'] is not None else 'commune inconnue'
        latitude = entry['latitude'] if entry['latitude'] is not None else 'latitude inconnue'
        longitude = entry['longitude'] if entry['longitude'] is not None else 'longitude inconnue'
        adresse_complet = f" {adresse} {code_postal} {commune} {latitude} {longitude}"
        type_service = entry['type_de_donnee']
        nom = entry['nom']

        context = f"Le {type_service} {nom} a pour adresse  {adresse_complet} "

        contexts.append(adresse_complet)

    return contexts


# Construire les contextes à partir des documents récupérés
contextes_batiments_services_questions = construire_contextes_batiments_services_questions(documents)
contextes_batiments_services_reponses = construire_contextes_batiments_services_reponses(documents2)



