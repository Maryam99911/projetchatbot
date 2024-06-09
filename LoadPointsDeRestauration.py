from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Sélectionner la base de données
db = client['ProjetChatbot']

# Sélectionner la collection
collection = db["PointsDeRestauration"]

# Récupérer les documents de la collection
documents = collection.find()

# Fonction pour construire les contextes
def construire_contextes_points_de_restauration(data):
    contexts = []
    for entry in data:
        site = entry.get('site', 'inconnu')
        restauration = entry.get('restauration', 'inconnu')
        adresse = entry.get('adresse', 'inconnu')
        cp = entry.get('cp', 'inconnu')
        ville = entry.get('ville', 'inconnu')
        poi = entry.get('poi', 'inconnu')

        context = (f"Au {site}, se trouve le restaurant {restauration}, situé à l'adresse {adresse}, {cp} {ville}. "
                   f"Les coordonnées GPS sont {poi['lat']}, {poi['lon']}.")
        contexts.append(context)
    return contexts

# Construire les contextes à partir des documents récupérés
contexts_points_de_restauration = construire_contextes_points_de_restauration(documents)

# Afficher les contextes pour vérification
for context in contexts_points_de_restauration:
    print(context)
