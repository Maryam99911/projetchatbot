from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Sélectionner la base de données
db = client['ProjetChatbot']

# Sélectionner la collection
collection = db['aides-financieres-cvec']

# Récupérer les documents de la collection
documents = collection.find()
documents2 = collection.find()


# Fonction pour construire les contextes
def construire_contextes_aides_financieres_questions(data):
    contexts = []
    for entry in data:
        annee = entry['annee_civile'].split('-')[0]
        nb_dossiers_deposes = entry['nb_dossiers_deposes']
        nb_dossiers_acceptes = entry['nb_dossiers_acceptes']
        budget = entry['budget']
        aide_moyenne = entry['aide_moyenne']

        context_dossiers_deposes = (f"Pendant l'annee {annee.lower()}, le <hl> nombre de dossiers déposés<hl> etait de  : {nb_dossiers_deposes}")
        contexts.append(context_dossiers_deposes)
        context_dossiers_acceptes = (f"Pendant l'annee {annee.lower()}, le <hl> nombre de dossiers acceptés<hl> etait de  : {nb_dossiers_acceptes}")
        contexts.append(context_dossiers_acceptes)
        context_budget = (f"Pendant l'annee {annee.lower()},  <hl> Le Budget<hl> etait de  : {budget}")
        contexts.append(context_budget)
        context_aide_moyenne = (f"Pendant l'annee {annee.lower()}, le <hl>L'Aide Moyenne du CVEC <hl> etait de :  {aide_moyenne}")
        contexts.append(context_aide_moyenne)

    return contexts


def construire_contextes_aides_financieres_reponses(data):
    contexts = []
    for entry in data:
        annee = entry['annee_civile'].split('-')[0]
        nb_dossiers_deposes = entry['nb_dossiers_deposes']
        nb_dossiers_acceptes = entry['nb_dossiers_acceptes']
        budget = entry['budget']
        aide_moyenne = entry['aide_moyenne']

        context_dossiers_deposes = (
            f"Pendant l'annee {annee.lower()}, le nombre de dossiers déposés etait de  {nb_dossiers_deposes}")
        contexts.append(context_dossiers_deposes)
        context_dossiers_acceptes = (
            f"Pendant l'annee {annee.lower()}, le nombre de dossiers acceptés etait de   {nb_dossiers_acceptes}")
        contexts.append(context_dossiers_acceptes)
        context_budget = (f"Pendant l'annee {annee.lower()}, le budget etait de   {budget}")
        contexts.append(context_budget)
        context_aide_moyenne = (
            f"Pendant l'annee {annee.lower()}, l'aide moyenne  etait de   {aide_moyenne}")
        contexts.append(context_aide_moyenne)

    return contexts

# Construire les contextes à partir des documents récupérés
contextes_aides_financieres_questions = construire_contextes_aides_financieres_questions(documents)
contextes_aides_financieres_reponses = construire_contextes_aides_financieres_reponses(documents2)


