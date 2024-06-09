from pymongo import MongoClient
import json

# Connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Sélectionner la base de données
db = client['ProjetChatbot']

# Sélectionner la collection
collection = db["ConsommationenEau"]

# Récupérer les documents de la collection
documents = collection.find()

def construire_contextes_consommation_eau(data):
    contexts = []
    for entry in data:
        location = entry.get('location', 'date inconnue')
        premiers_cycles = entry.get('batiment_premiers_cycles', 'donnée inconnue')
        iut_romero = entry.get('batiment_iut_romero', 'donnée inconnue')
        bibliotheque_universitaire = entry.get('batiment_bibliotheque_universitaire', 'donnée inconnue')
        facteur_cheval = entry.get('batiment_facteur_cheval', 'donnée inconnue')
        ibgbi = entry.get('batiment_ibgbi', 'donnée inconnue')
        ile_de_france = entry.get('batiment_ile_de_france', 'donnée inconnue')
        maupertuis = entry.get('batiment_maupertuis', 'donnée inconnue')
        iut_romero0 = entry.get('batiment_iut_romero0', 'donnée inconnue')

        context = (f"Pour la date {location}, la consommation d'eau est la suivante :\n"
                   f"- Premiers cycles : {premiers_cycles}\n"
                   f"- IUT Roméro : {iut_romero}\n"
                   f"- Bibliothèque Universitaire : {bibliotheque_universitaire}\n"
                   f"- Facteur Cheval : {facteur_cheval}\n"
                   f"- IBGBI : {ibgbi}\n"
                   f"- Île de France : {ile_de_france}\n"
                   f"- Maupertuis : {maupertuis}\n"
                   f"- IUT Roméro 0 : {iut_romero0}")

        contexts.append(context)
    return contexts

# Construire les contextes à partir des documents récupérés
contexts_consommation_eau = construire_contextes_consommation_eau(documents)

# Afficher les contextes pour vérification
for context in contexts_consommation_eau:
    print(context)
