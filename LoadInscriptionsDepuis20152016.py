from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Sélectionner la base de données
db = client['ProjetChatbot']

# Sélectionner la collection
collection = db["InscriptionsDepuis2015-2016"]

# Récupérer les documents de la collection
documents = collection.find()

# Fonction pour construire les contextes
def construire_contextes_inscriptions_depuis_2015(data):
    contexts = []
    for entry in data:
        annee_universitaire = entry.get('annee_universitaire', 'inconnu')
        iprincipales = entry.get('iprincipales', 'inconnu')
        itotales_avec_doubles = entry.get('itotales_avec_doubles', 'inconnu')
        dont_boursiers = entry.get('dont_boursiers', 'inconnu')
        dont_cursus_l = entry.get('dont_cursus_l', 'inconnu')
        dont_cursus_m = entry.get('dont_cursus_m', 'inconnu')
        dont_cursus_d = entry.get('dont_cursus_d', 'inconnu')
        dont_neo_bacheliers = entry.get('dont_neo_bacheliers', 'inconnu')
        dont_oui_si = entry.get('dont_oui_si', 'inconnu')
        dont_neo_entrants = entry.get('dont_neo_entrants', 'inconnu')
        dont_paris_saclay = entry.get('dont_paris_saclay', 'inconnu')
        dont_ecole_paris_saclay = entry.get('dont_ecole_paris_saclay', 'inconnu')
        dont_ueve = entry.get('dont_ueve', 'inconnu')
        dont_iut = entry.get('dont_iut', 'inconnu')
        dont_ufr_sfa = entry.get('dont_ufr_sfa', 'inconnu')
        dont_ufr_st = entry.get('dont_ufr_st', 'inconnu')
        dont_ufr_shs = entry.get('dont_ufr_shs', 'inconnu')
        dont_ufr_lam = entry.get('dont_ufr_lam', 'inconnu')
        dont_ufr_dsp = entry.get('dont_ufr_dsp', 'inconnu')

        context = (f"Pour l'année universitaire {annee_universitaire}, le nombre d'inscriptions principales est de {iprincipales}, "
                   f"et le nombre total d'inscriptions avec doubles est de {itotales_avec_doubles}. "
                   f"Le nombre de boursiers est de {dont_boursiers}. "
                   f"Le nombre d'inscriptions en cursus L est de {dont_cursus_l}, en cursus M est de {dont_cursus_m}, et en cursus D est de {dont_cursus_d}. "
                   f"Le nombre de néobacheliers est de {dont_neo_bacheliers}, dont {dont_oui_si} Oui-Si. "
                   f"Le nombre de néo-entrants est de {dont_neo_entrants}. "
                   f"Les inscriptions à Paris-Saclay sont de {dont_paris_saclay}, dont {dont_ecole_paris_saclay} à l'École de Paris-Saclay. "
                   f"Les inscriptions à l'UEVE sont de {dont_ueve}, dont {dont_iut} à l'IUT, {dont_ufr_sfa} à l'UFR SFA, {dont_ufr_st} à l'UFR ST, "
                   f"{dont_ufr_shs} à l'UFR SHS, {dont_ufr_lam} à l'UFR LAM, et {dont_ufr_dsp} à l'UFR DSP.")
        contexts.append(context)
    return contexts

# Construire les contextes à partir des documents récupérés
contexts_inscriptions_depuis_2015 = construire_contextes_inscriptions_depuis_2015(documents)

# Afficher les contextes pour vérification
for context in contexts_inscriptions_depuis_2015:
    print(context)
