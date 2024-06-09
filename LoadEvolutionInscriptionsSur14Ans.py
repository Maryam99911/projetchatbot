from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Sélectionner la base de données
db = client['ProjetChatbot']

# Sélectionner la collection
collection = db["EvolutionInscriptionsSur14Ans"]

# Récupérer les documents de la collection
documents = collection.find()

# Fonction pour construire les contextes
def construire_contextes_evolution_inscriptions(data):
    contexts = []
    for entry in data:
        annee_universitaire = entry.get('annee_universitaire', 'inconnu')
        cursus_l = entry.get('cursus_l', 'inconnu')
        cursus_m = entry.get('cursus_m', 'inconnu')
        cursus_d = entry.get('cursus_d', 'inconnu')
        nombre_d_etudiants = entry.get('nombre_d_etudiants', 'inconnu')
        nombre_neobacheliers = entry.get('nombre_neobacheliers', 'inconnu')
        nombre_de_neorentrants = entry.get('nombre_de_neorentrants', 'inconnu')

        context = (f"Pour l'année universitaire {annee_universitaire}, le nombre d'étudiants en cursus L est de {cursus_l}, "
                   f"en cursus M est de {cursus_m}, et en cursus D est de {cursus_d}. "
                   f"Le nombre total d'étudiants est de {nombre_d_etudiants}, "
                   f"avec {nombre_neobacheliers} néobacheliers et {nombre_de_neorentrants} néorentrants.")
        contexts.append(context)
    return contexts

# Construire les contextes à partir des documents récupérés
contexts_evolution_inscriptions = construire_contextes_evolution_inscriptions(documents)

# Afficher les contextes pour vérification
for context in contexts_evolution_inscriptions:
    print(context)
