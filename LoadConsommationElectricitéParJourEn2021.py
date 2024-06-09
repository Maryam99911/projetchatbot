from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Sélectionner la base de données
db = client['ProjetChatbot']

# Sélectionner la collection
collection = db["ConsommationElectricitéParJourEn2021"]

# Récupérer les documents de la collection
documents = collection.find()

def construire_contextes_consommation_electricite(data):
    contexts = []
    for entry in data:
        location = entry.get('location', 'lieu inconnu')
        maupertuis = entry.get('batiment_maupertuis', 'inconnu')
        bibliotheque = entry.get('batiment_bibliotheque_universitaire', 'inconnu')
        pelvoux = entry.get('iup_pelvoux', 'inconnu')
        romero = entry.get('batiment_iut_romero', 'inconnu')
        rostand = entry.get('iut_rostand', 'inconnu')
        ibgbi = entry.get('batiment_ibgbi', 'inconnu')
        premiers_cycles = entry.get('batiment_premiers_cycles', 'inconnu')
        facteur_cheval = entry.get('batiment_facteur_cheval', 'inconnu')
        ile_de_france = entry.get('batiment_ile_de_france', 'inconnu')
        bretigny = entry.get('iut_bretigny', 'inconnu')

        context = (f"Pour la date '{location}', la consommation d'électricité était de :\n"
                   f"- Maupertuis : {maupertuis} kWh\n"
                   f"- Bibliothèque Universitaire : {bibliotheque} kWh\n"
                   f"- IUP Pelvoux : {pelvoux} kWh\n"
                   f"- IUT Romero : {romero} kWh\n"
                   f"- IUT Rostand : {rostand} kWh\n"
                   f"- IBGBI : {ibgbi} kWh\n"
                   f"- Premiers Cycles : {premiers_cycles} kWh\n"
                   f"- Facteur Cheval : {facteur_cheval} kWh\n"
                   f"- Île de France : {ile_de_france} kWh\n"
                   f"- IUT Brétigny : {bretigny} kWh")
        contexts.append(context)
    return contexts

# Construire les contextes à partir des documents récupérés
contexts_consommation_electricite = construire_contextes_consommation_electricite(documents)

# Afficher les contextes pour vérification
for context in contexts_consommation_electricite:
    print(context)
