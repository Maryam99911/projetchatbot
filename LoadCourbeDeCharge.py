from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Sélectionner la base de données
db = client['ProjetChatbot']

# Sélectionner la collection
collection = db['CourbeDeCharge']

# Récupérer les documents de la collection
documents = collection.find()

def construire_contextes_courbe_charge(data):
    contexts = []
    for entry in data:
        location = entry.get('location', 'emplacement inconnu')
        maupertuis = entry.get('batiment_maupertuis', 'inconnu')
        bibliotheque = entry.get('batiment_bibliotheque_universitaire', 'inconnue')
        pelvoux = entry.get('iup_pelvoux', 'inconnu')
        romero = entry.get('batiment_iut_romero', 'inconnu')
        ibgbi = entry.get('batiment_ibgbi', 'inconnu')
        cycles = entry.get('batiment_premiers_cycles', 'inconnus')
        cheval = entry.get('batiment_facteur_cheval', 'inconnu')
        ile_france = entry.get('batiment_ile_de_france', 'inconnue')
        bretigny = entry.get('iut_bretigny', 'inconnu')

        context = (f"À l'emplacement {location}, les données de charge sont : "
                   f"Maupertuis: {maupertuis}, "
                   f"Bibliothèque Universitaire: {bibliotheque}, "
                   f"IUP Pelvoux: {pelvoux}, "
                   f"Bâtiment IUT Romero: {romero}, "
                   f"Bâtiment IBGBI: {ibgbi}, "
                   f"Bâtiment Premiers Cycles: {cycles}, "
                   f"Bâtiment Facteur Cheval: {cheval}, "
                   f"Bâtiment Île de France: {ile_france}, "
                   f"IUT Brétigny: {bretigny}.")
        contexts.append(context)
    return contexts

# Construire les contextes à partir des documents récupérés
contexts_courbe_charge = construire_contextes_courbe_charge(documents)

# Afficher les contextes pour vérification
for context in contexts_courbe_charge:
    print(context)
