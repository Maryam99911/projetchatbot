from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Sélectionner la base de données
db = client['ProjetChatbot']

# Sélectionner la collection
collection = db["LocalisationDistributeursDeProtection"]

# Récupérer les documents de la collection
documents = collection.find()

# Fonction pour construire les contextes
def construire_contextes_localisation_distributeurs(data):
    contexts = []
    for entry in data:
        code_etablissement = entry.get('code_etablissement', 'inconnu')
        appellation_officielle = entry.get('appellation_officielle', 'inconnu')
        trie_coll_lycee = entry.get('trie_coll_lycee', 'inconnu')
        coll_0_lyc_1 = entry.get('coll_0_lyc_1', 'inconnu')
        denomination_principale = entry.get('denomination_principale', 'inconnu')
        patronyme_uai = entry.get('patronyme_uai', 'inconnu')
        secteur_public_prive = entry.get('secteur_public_prive', 'inconnu')
        adresse = entry.get('adresse', 'inconnu')
        lieu_dit = entry.get('lieu_dit', 'inconnu')
        boite_postale = entry.get('boite_postale', 'inconnu')
        code_postal = entry.get('code_postal', 'inconnu')
        localite_d_acheminement = entry.get('localite_d_acheminement', 'inconnu')
        commune = entry.get('commune', 'inconnu')
        coordonnee_x = entry.get('coordonnee_x', 'inconnu')
        coordonnee_y = entry.get('coordonnee_y', 'inconnu')
        epsg = entry.get('epsg', 'inconnu')
        latitude = entry.get('latitude', 'inconnu')
        longitude = entry.get('longitude', 'inconnu')
        qualite_d_appariement = entry.get('qualite_d_appariement', 'inconnu')
        localisation = entry.get('localisation', 'inconnu')
        code_nature = entry.get('code_nature', 'inconnu')
        nature = entry.get('nature', 'inconnu')
        code_etat_etablissement = entry.get('code_etat_etablissement', 'inconnu')
        etat_etablissement = entry.get('etat_etablissement', 'inconnu')
        code_departement = entry.get('code_departement', 'inconnu')
        code_region = entry.get('code_region', 'inconnu')
        code_academie = entry.get('code_academie', 'inconnu')
        code_commune = entry.get('code_commune', 'inconnu')
        departement = entry.get('departement', 'inconnu')
        region = entry.get('region', 'inconnu')
        academie = entry.get('academie', 'inconnu')
        position = entry.get('position', 'inconnu')
        secteur_prive_code_type_contrat = entry.get('secteur_prive_code_type_contrat', 'inconnu')
        secteur_prive_libelle_type_contrat = entry.get('secteur_prive_libelle_type_contrat', 'inconnu')
        code_ministere = entry.get('code_ministere', 'inconnu')
        libelle_ministere = entry.get('libelle_ministere', 'inconnu')
        date_ouverture = entry.get('date_ouverture', 'inconnu')
        pos_geo = entry.get('pos_geo', 'inconnu')
        poi = entry.get('poi', 'inconnu')

        context = (f"Pour l'établissement {appellation_officielle}, code {code_etablissement}, de type {denomination_principale}, "
                   f"situé à {adresse}, {code_postal} {localite_d_acheminement}, commune de {commune}. "
                   f"Cet établissement est un {trie_coll_lycee}, de nature {secteur_public_prive}. "
                   f"Les coordonnées GPS sont {latitude}, {longitude}. "
                   f"Le code EPSG est {epsg}. "
                   f"Le code de nature est {code_nature} ({nature}). "
                   f"L'état de l'établissement est {etat_etablissement}. "
                   f"Il est situé dans le département {departement}, la région {region} et l'académie {academie}. "
                   f"La position géographique est {position}. "
                   f"Le secteur privé est {secteur_prive_libelle_type_contrat} ({secteur_prive_code_type_contrat}). "
                   f"Ce lieu est placé sous le ministère {libelle_ministere} ({code_ministere}). "
                   f"Il a ouvert ses portes le {date_ouverture}. "
                   f"Les coordonnées géographiques sont {pos_geo}. "
                   f"Les Points d'Intérêt (POI) sont {poi}.")
        contexts.append(context)
    return contexts

# Construire les contextes à partir des documents récupérés
contexts_localisation_distributeurs = construire_contextes_localisation_distributeurs(documents)

# Afficher les contextes pour vérification
for context in contexts_localisation_distributeurs:
    print(context)
