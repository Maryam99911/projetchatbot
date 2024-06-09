from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Sélectionner la base de données
db = client['ProjetChatbot']

# Sélectionner la collection
collection = db['associations-etudiantes']

# Récupérer les documents de la collection
documents = collection.find()

# Fonction pour construire les contextes
def construire_contextes_associations(data):
    contexts = []
    for entry in data:
        # Gestion des valeurs None ou manquantes
        code_postal = int(entry['code_postal']) if entry.get('code_postal') is not None else 'inconnu'
        numero_de_voie = int(entry['numero_de_voie']) if entry.get('numero_de_voie') is not None else 'inconnu'
        voie = entry.get('voie', 'voie inconnue')
        site_web = entry.get('site_web', 'pas de site web')
        reseaux_sociaux = entry.get('reseaux_sociaux', 'pas de réseaux sociaux')

        context = (f"L'association {entry['nom']} ({entry['sigle']}) située à {entry['commune']} "
                   f"dans le code postal {code_postal} {voie} {numero_de_voie}, "
                   f"présidée par {entry['president']}, a pour objectif {entry['description']}. "
                   f"Vous pouvez en savoir plus sur leur site web : {site_web} "
                   f"ou les suivre sur leurs réseaux sociaux : {reseaux_sociaux}.")
        contexts.append(context)
    return contexts

# Construire les contextes à partir des documents récupérés
contexts_associations = construire_contextes_associations(documents)

# Afficher les contextes pour vérification
for context in contexts_associations:
    print(context)
