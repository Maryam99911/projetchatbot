from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Sélectionner la base de données
db = client['ProjetChatbot']

# Sélectionner la collection
collection = db["NombreInscritsParCursus"]

# Récupérer les documents de la collection
documents = collection.find()

# Fonction pour construire les contextes
def construire_contextes_nombre_inscrits_par_cursus(data):
    contexts = []
    for entry in data:
        annee_de_linscription = entry.get('annee_de_linscription', 'inconnu')
        cursus_lmd = entry.get('cursus_lmd', 'inconnu')
        niveau = entry.get('niveau', 'inconnu')
        somme_nombre_etudiants = entry.get('somme_nombre_etudiants', 'inconnu')

        context = (f"Pour l'année {annee_de_linscription}, {somme_nombre_etudiants} étudiant(s) ont été inscrit(s) en {niveau}, dans le cursus {cursus_lmd}.")
        contexts.append(context)
    return contexts

# Construire les contextes à partir des documents récupérés
contexts_nombre_inscrits_par_cursus = construire_contextes_nombre_inscrits_par_cursus(documents)

# Afficher les contextes pour vérification
for context in contexts_nombre_inscrits_par_cursus:
    print(context)
