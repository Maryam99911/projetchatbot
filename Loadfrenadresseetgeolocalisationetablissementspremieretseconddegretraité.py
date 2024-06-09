from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Sélectionner la base de données
db = client['ProjetChatbot']

# Sélectionner la collection
collection = db["fr-en-adresse-et-geolocalisation-etablissements-premier-et-second-degre_traité"]

# Récupérer les documents de la collection
documents = collection.find()

# Fonction pour construire les contextes
def construire_contextes_etablissements_scolaires(data):
    contexts = []
    for entry in data:
        rentree_scolaire = entry.get('rentree_scolaire', 'inconnue')
        denomination_principale = entry.get('denomination_principale', 'inconnue')
        patronyme = entry.get('patronyme', 'inconnu')
        secteur = entry.get('secteur', 'inconnu')
        numero_etablissement = entry.get('numero_etablissement', 'inconnu')
        nombre_eleves_total = entry.get('nombre_d_eleves_total_nombre_d_eleves_dans_les_formations_du_1er_cycle_du_2nd_degre_et_non_du_nombre', 'inconnu')
        localisation = entry.get('localisation', {})
        ips_ensemble_gt_pro_2022 = entry.get('ips_ensemble_gt_pro_2022', 'inconnu')
        url = entry.get('url', 'inconnue')

        context = (f"{denomination_principale} '{patronyme}' est un établissement {secteur} "
                   f"qui a accueilli un total de {nombre_eleves_total} élèves pour la rentrée scolaire {rentree_scolaire}. "
                   f"Son numéro d'établissement est {numero_etablissement}. ")
        if localisation:
            context += f"Voici sa localisation géographique : latitude {localisation.get('lat', 'inconnue')} et longitude {localisation.get('lon', 'inconnue')}. "
        if ips_ensemble_gt_pro_2022 != 'inconnu':
            context += f"Son indicateur de positionnement sur le taux de réussite global est de {ips_ensemble_gt_pro_2022} en 2022. "
        context += f"Plus d'informations peuvent être trouvées sur son URL : {url}."
        contexts.append(context)
    return contexts

# Construire les contextes à partir des documents récupérés
contexts_etablissements_scolaires = construire_contextes_etablissements_scolaires(documents)

# Afficher les contextes pour vérification
for context in contexts_etablissements_scolaires:
    print(context)
