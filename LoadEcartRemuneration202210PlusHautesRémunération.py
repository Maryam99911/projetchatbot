from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Sélectionner la base de données
db = client['ProjetChatbot']

# Sélectionner la collection
collection = db["EcartRemuneration2022-10PlusHautesRémunération"]

# Récupérer les documents de la collection
documents = collection.find()

def construire_contextes_ecart_remuneration(data):
    contexts = []
    for entry in data:
        nombre_de_femmes = entry.get('nombre_de_femmes_beneficiaires', 'nombre de femmes inconnu')
        nombre_d_hommes = entry.get('nombre_d_hommes_beneficiaires', 'nombre d\'hommes inconnu')
        population_sous_representee = entry.get('effectif_de_la_population_sous_representee', 'effectif de la population sous-représentée inconnu')
        score = entry.get('score_sur_20', 'score inconnu')

        context = f"Pour l'Ecart de Remuneration en 2022 - 10 Plus Hautes Rémunérations : Pour cette analyse, il y a {nombre_de_femmes} femmes et {nombre_d_hommes} hommes bénéficiaires. " \
                  f"Le nombre d'effectif de la population sous-représentée est de {population_sous_representee}. " \
                  f"Le score sur 20 est de {score}."
        contexts.append(context)
    return contexts

# Construire les contextes à partir des documents récupérés
contexts_ecart_remuneration = construire_contextes_ecart_remuneration(documents)

# Afficher les contextes pour vérification
for context in contexts_ecart_remuneration:
    print(context)
