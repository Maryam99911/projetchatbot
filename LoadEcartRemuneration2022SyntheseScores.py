from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Sélectionner la base de données
db = client['ProjetChatbot']

# Sélectionner la collection
collection = db["EcartRemuneration2022-SyntheseScores"]

# Récupérer les documents de la collection
documents = collection.find()

# Fonction pour construire les contextes
def construire_contextes_synthese_scores(data):
    contexts = []
    for entry in data:
        indicateurs = entry.get('indicateurs', 'inconnu')
        note_maximale_initiale = entry.get('note_maximale_initiale', 'inconnu')
        score_initial_de_l_ep = entry.get('score_initial_de_l_ep', 'inconnu')

        context = (f"Pour l'indicateur '{indicateurs}', la note maximale initiale est de {note_maximale_initiale}, "
                   f"et le score initial de l'EP est de {score_initial_de_l_ep}.")
        contexts.append(context)
    return contexts

# Construire les contextes à partir des documents récupérés
contexts_synthese_scores = construire_contextes_synthese_scores(documents)

# Afficher les contextes pour vérification
for context in contexts_synthese_scores:
    print(context)
