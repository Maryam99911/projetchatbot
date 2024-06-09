from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Sélectionner la base de données
db = client['ProjetChatbot']

# Sélectionner la collection
collection = db['AidesNumeriques']

# Récupérer les documents de la collection
documents = collection.find()

# Fonction pour construire les contextes
def construire_contextes_aides_financieres(data):
    contexts = []
    for entry in data:
        annee = entry['annee_civile'].split('-')[0]
        context = (f"En {annee}, il y avait {entry['nb_dossiers_deposes']} dossiers déposés, "
                   f"{entry['nb_dossiers_acceptes']} dossiers acceptés, avec un budget de "
                   f"{entry['budget']} euros et une aide moyenne de {entry['aide_moyenne']} euros "
                   f"pour le type de financement {entry['type']}.")
        contexts.append(context)
    return contexts

# Construire les contextes à partir des documents récupérés
contexts_aides_financieres = construire_contextes_aides_financieres(documents)

# Afficher les contextes pour vérification
for context in contexts_aides_financieres:
    print(context)
