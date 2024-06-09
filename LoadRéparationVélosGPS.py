from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Sélectionner la base de données
db = client['ProjetChatbot']

# Sélectionner la collection
collection = db["RéparationVélosGPS"]

# Récupérer les documents de la collection
documents = collection.find()

# Fonction pour construire les contextes
def construire_contextes_reparation_velos_gps(data):
    contexts = []
    for entry in data:
        etablissement = entry.get('etablissement', 'inconnu')
        adresse = entry.get('adresse', 'inconnu')
        code_insee = entry.get('code_insee', 'inconnu')
        commune = entry.get('commune', 'inconnu')
        telephone = entry.get('telephone', 'inconnu')
        site_web = entry.get('site_web', 'inconnu')
        complement = entry.get('complement', 'inconnu')
        geopoint = entry.get('geopoint', 'inconnu')

        context = (f"L'établissement '{etablissement}' propose des services de réparation de vélos. "
                   f"Il est situé à l'adresse : {adresse}, {code_insee} {commune}. ")
        if complement:
            context += f"{complement}. "
        context += f"Vous pouvez les contacter au {telephone} ou visiter leur site web : {site_web}. "
        if geopoint:
            context += f"Les coordonnées GPS sont {geopoint['lat']}, {geopoint['lon']}."
        contexts.append(context)
    return contexts

# Construire les contextes à partir des documents récupérés
contexts_reparation_velos_gps = construire_contextes_reparation_velos_gps(documents)

# Afficher les contextes pour vérification
for context in contexts_reparation_velos_gps:
    print(context)
