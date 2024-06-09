from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Sélectionner la base de données
db = client['ProjetChatbot']

# Sélectionner la collection
collection = db["ChiffresClésSurL'universitéD'evry"]


# Récupérer les documents de la collection
documents = collection.find()

def construire_contextes_chiffres_cles(data):
    contexts = []
    for entry in data:
        theme = entry.get('theme', 'thème inconnu')
        chiffres = entry.get('chiffres', 'chiffres inconnus')
        variables = entry.get('variables', 'variables inconnues')

        context = f"Pour le thème '{theme}', il y a {chiffres} {variables}."
        contexts.append(context)
    return contexts

# Construire les contextes à partir des documents récupérés
contexts_chiffres_cles = construire_contextes_chiffres_cles(documents)

# Afficher les contextes pour vérification
for context in contexts_chiffres_cles:
    print(context)
