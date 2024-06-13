from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Sélectionner la base de données
db = client['ProjetChatbot']

# Sélectionner la collection
collection = db["TauxDeRéussite"]

# Récupérer les documents de la collection
documents = collection.find()
documents2 = collection.find()


# Fonction pour construire les contextes
def construire_contextes_taux_de_reussite_questions(data):
    contexts = []
    for entry in data:
        domaine = entry.get('domaine', 'inconnu')
        etape = entry.get('etape', 'inconnu')
        annee_de_l_inscription = entry.get('annee_de_l_inscription', 'inconnu')

        context = (f"Quelle est le taux de reussite dans le domaine '{domaine}', pour l'étape '{etape}' et l'année d'inscription ' {annee_de_l_inscription}")
        contexts.append(context)
    return contexts

def construire_contextes_taux_de_reussite_reponses(data):
    contexts = []
    for entry in data:
        domaine = entry.get('domaine', 'inconnu')
        etape = entry.get('etape', 'inconnu')
        annee_de_l_inscription = entry.get('annee_de_l_inscription', 'inconnu')
        taux_de_reussite = entry.get('taux_de_reussite0', 'inconnu')

        context = (f"Dans le domaine '{domaine}', pour l'étape '{etape}' et l'année d'inscription '{annee_de_l_inscription} ', "
                   f"le taux de réussite est de  {taux_de_reussite}%.")
        contexts.append(context)
    return contexts

# Construire les contextes à partir des documents récupérés
contexts_taux_reussite_questions = construire_contextes_taux_de_reussite_questions(documents)
contexts_taux_reussite_reponses = construire_contextes_taux_de_reussite_reponses(documents2)



