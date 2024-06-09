from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Sélectionner la base de données
db = client['ProjetChatbot']

# Sélectionner la collection
collection = db["ConsommationChauffageUrbain"]

# Récupérer les documents de la collection
documents = collection.find()

def construire_contextes_consommation_chauffage(data):
    contexts = []
    for entry in data:
        location = entry.get('location', 'date inconnue')
        batiment_ile_de_france = entry.get('batiment_ile_de_france', 'inconnu')
        batiment_bibliotheque_universitaire = entry.get('batiment_bibliotheque_universitaire', 'inconnu')
        batiment_ibgbi = entry.get('batiment_ibgbi', 'inconnu')
        batiment_maupertuis = entry.get('batiment_maupertuis', 'inconnu')
        batiment_premiers_cycles = entry.get('batiment_premiers_cycles', 'inconnu')
        batiment_facteur_cheval = entry.get('batiment_facteur_cheval', 'inconnu')

        context = (f"Pour la date {location}, la consommation de chauffage urbain est la suivante :\n"
                   f"- Batiment Île de France : {batiment_ile_de_france}\n"
                   f"- Batiment Bibliothèque Universitaire : {batiment_bibliotheque_universitaire}\n"
                   f"- Batiment IBGBI : {batiment_ibgbi}\n"
                   f"- Batiment Maupertuis : {batiment_maupertuis}\n"
                   f"- Batiment Premiers Cycles : {batiment_premiers_cycles}\n"
                   f"- Batiment Facteur Cheval : {batiment_facteur_cheval}")
        contexts.append(context)
    return contexts

# Construire les contextes à partir des documents récupérés
contexts_consommation_chauffage = construire_contextes_consommation_chauffage(documents)

# Afficher les contextes pour vérification
for context in contexts_consommation_chauffage:
    print(context)
