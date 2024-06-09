from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Sélectionner la base de données
db = client['ProjetChatbot']

# Sélectionner la collection
collection = db['CaractéristiquesDesEtudiants']

# Récupérer les documents de la collection
documents = collection.find()

def construire_contextes_etudiants(data):
    contexts = []
    for entry in data:
        annee_inscription = entry.get('annee_de_linscription', 'année d\'inscription inconnue')
        genre = entry.get('genre', 'genre inconnu')
        cursus = entry.get('cursus_lmd', 'cursus inconnu')
        regime_inscription = entry.get('regime_d_inscription', 'régime d\'inscription inconnu')
        domaine_formation = entry.get('domaine_de_formation', 'domaine de formation inconnu')
        type_bac_obtenu = entry.get('type_de_bac_obtenu', 'type de baccalauréat inconnu')
        nb_etudiants = entry.get('nombre_d_etudiants', 'nombre d\'étudiants inconnu')
        nb_nouveaux_bacheliers = entry.get('nombre_de_nouveaux_bacheliers', 'nombre de nouveaux bacheliers inconnu')

        context = (f"Pour l'{annee_inscription}, {nb_etudiants} étudiants ont été inscrits, dont "
                   f"{nb_nouveaux_bacheliers} nouveaux bacheliers. Ils sont principalement de genre {genre}, inscrits "
                   f"dans le cursus {cursus}, de régime d'inscription {regime_inscription}, et étudient dans le domaine "
                   f"{domaine_formation}. Le type de baccalauréat obtenu par ces étudiants est {type_bac_obtenu}.")
        contexts.append(context)
    return contexts

# Construire les contextes à partir des documents récupérés
contexts_etudiants = construire_contextes_etudiants(documents)

# Afficher les contextes pour vérification
for context in contexts_etudiants:
    print(context)

