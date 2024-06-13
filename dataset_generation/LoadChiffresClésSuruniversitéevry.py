from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Sélectionner la base de données
db = client['ProjetChatbot']

# Sélectionner la collection
collection = db["ChiffresClésSurL'universitéD'evry"]


# Récupérer les documents de la collection
documents = collection.find()
documents2 = collection.find()

def construire_contextes_chiffres_cles_questions(data):
    contexts = []
    for entry in data:
        theme = entry.get('theme', 'thème inconnu')
        chiffres = entry.get('chiffres', 'chiffres inconnus')
        variables = entry.get('variables', 'variables inconnues')

        context = f"Pour le thème '{theme}', il y a <hl>{chiffres}<hl> {variables}."
        contexts.append(context)
    return contexts

def construire_contextes_chiffres_cles_reponses(data):
    contexts = []
    for entry in data:
        theme = entry.get('theme', 'thème inconnu')
        chiffres = entry.get('chiffres', 'chiffres inconnus')
        variables = entry.get('variables', 'variables inconnues')
        context = f"Pour le thème '{theme}', il y a {chiffres} {variables}."
        contexts.append(context)
    return contexts
# Construire les contextes à partir des documents récupérés

contexts_chiffres_cles_universite_questions = construire_contextes_chiffres_cles_questions(documents)
contexts_chiffres_cles_universite_reponses = construire_contextes_chiffres_cles_reponses(documents2)

