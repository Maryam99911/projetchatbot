from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Sélectionner la base de données
db = client['ProjetChatbot']

# Sélectionner la collection
collection = db["NombreD'inscritsParBac"]

# Récupérer les documents de la collection
documents = collection.find()

# Fonction pour construire les contextes
def construire_contextes_nombre_inscrits_par_bac(data):
    contexts = []
    for entry in data:
        annee_de_linscription = entry.get('annee_de_linscription', 'inconnu')
        groupe_de_bac = entry.get('groupe_de_bac', 'inconnu')
        bac_serie = entry.get('bac_serie', 'inconnu')
        niveau = entry.get('niveau', 'inconnu')
        somme_de_nombre_etudiants = entry.get('somme_de_nombre_etudiants', 'inconnu')

        context = (f"Pour l'année {annee_de_linscription}, {somme_de_nombre_etudiants} étudiants ont été inscrits en {niveau} ayant passé le bac série {bac_serie} du groupe {groupe_de_bac}.")
        contexts.append(context)
    return contexts

# Construire les contextes à partir des documents récupérés
contexts_nombre_inscrits_par_bac = construire_contextes_nombre_inscrits_par_bac(documents)

# Afficher les contextes pour vérification
for context in contexts_nombre_inscrits_par_bac:
    print(context)
