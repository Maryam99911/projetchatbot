from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Sélectionner la base de données
db = client['ProjetChatbot']

# Sélectionner la collection
collection = db['CaractéristiquesDesEtudiants']



# Création d'un index sur le champ 'annee_de_linscription'
collection.create_index([('annee_de_linscription', 1)])

# Pipeline d'agrégation pour regrouper les données par 'domaine_de_formation'
pipeline_2022_2023 = [
    {'$match': {'annee_de_linscription': '2022/2023'}},
    {
        '$group': {
            '_id': '$domaine_de_formation',
            'nombre_total_d_etudiants': {'$sum': '$nombre_d_etudiants'},
            'nombre_total_de_nouveaux_bacheliers': {'$sum': '$nombre_de_nouveaux_bacheliers'}
        }
    },
    {
        '$project': {
            '_id': 0,
            'domaine_de_formation': '$_id',
            'nombre_total_d_etudiants': 1,
            'nombre_total_de_nouveaux_bacheliers': 1
        }
    }
]

# Exécuter l'agrégation
result2023_pipeline = collection.aggregate(pipeline_2022_2023)

# Récupérer les documents de la collection

documents = collection.find()

def construire_contextes_etudiants_questions_reponses(pipeline,annee):
    contexts_questions = []
    contexts_reponses = []
    for ligne in pipeline :
        question_domaine = f"Pour l'annee {annee}, combien d'etudiants était inscrit dans la formation {ligne['domaine_de_formation']}?"
        context_domaine = f"Pour l'annee {annee}, le nombre total d'étudiants est de {ligne['nombre_total_d_etudiants']} dont {ligne['nombre_total_de_nouveaux_bacheliers']} nouveaux bacheliers dans le domaine {ligne['domaine_de_formation']}"
        question_bachelier = f"Pour l'annee {annee}, combien de nouveaux bacheliers y'avait-il dans la formation  {ligne['domaine_de_formation']}?"
        context_bachelier = f"Pour l'annee {annee}, le nombre total nouveaux bacheliers dans le domaine {ligne['domaine_de_formation']} est de {ligne['nombre_total_de_nouveaux_bacheliers']}  "
        contexts_questions.append(question_domaine)
        contexts_questions.append(question_bachelier)
        contexts_reponses.append(context_domaine)
        contexts_reponses.append(context_bachelier)

    return contexts_questions,contexts_reponses

# Construire les contextes à partir des documents récupérés
contexts_caracteristiques_etudiants_questions_2023,  contexts_caracteristiques_etudiants_reponses_2023= construire_contextes_etudiants_questions_reponses(result2023_pipeline,'2022/2023')




