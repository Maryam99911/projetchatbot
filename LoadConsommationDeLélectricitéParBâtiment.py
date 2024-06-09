from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Sélectionner la base de données
db = client['ProjetChatbot']

# Sélectionner la collection
collection = db["ConsommationDeL'électricitéParBâtiment"]

# Récupérer les documents de la collection
documents = collection.find()

def construire_contextes_consommation_electricite(data):
    contexts = []
    for entry in data:
        location = entry.get('location', 'date inconnue')
        maupertuis = entry.get('batiment_maupertuis', 'consommation inconnue')
        bibliotheque_universitaire = entry.get('batiment_bibliotheque_universitaire', 'consommation inconnue')
        pelvoux = entry.get('iup_pelvoux', 'consommation inconnue')
        iut_romero = entry.get('batiment_iut_romero', 'consommation inconnue')
        iut_rostand = entry.get('iut_rostand', 'consommation inconnue')
        ibgbi = entry.get('batiment_ibgbi', 'consommation inconnue')
        premiers_cycles = entry.get('batiment_premiers_cycles', 'consommation inconnue')
        facteur_cheval = entry.get('batiment_facteur_cheval', 'consommation inconnue')
        ile_de_france = entry.get('batiment_ile_de_france', 'consommation inconnue')
        iut_bretigny = entry.get('iut_bretigny', 'consommation inconnue')

        context = (f"Pour la date '{location}', la consommation d'électricité par bâtiment est la suivante : "
                   f"- Maupertuis : {maupertuis} kWh\n"
                   f"- Bibliothèque Universitaire : {bibliotheque_universitaire} kWh\n"
                   f"- IUP Pelvoux : {pelvoux} kWh\n"
                   f"- IUT Romero : {iut_romero} kWh\n"
                   f"- IUT Rostand : {iut_rostand} kWh\n"
                   f"- IBGBI : {ibgbi} kWh\n"
                   f"- Premiers Cycles : {premiers_cycles} kWh\n"
                   f"- Facteur Cheval : {facteur_cheval} kWh\n"
                   f"- Île de France : {ile_de_france} kWh\n"
                   f"- IUT Brétigny : {iut_bretigny} kWh")
        contexts.append(context)
    return contexts

# Construire les contextes à partir des documents récupérés
contexts_consommation_electricite = construire_contextes_consommation_electricite(documents)

# Afficher les contextes pour vérification
for context in contexts_consommation_electricite:
    print(context)
