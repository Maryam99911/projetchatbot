from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Sélectionner la base de données
db = client['ProjetChatbot']

# Sélectionner la collection
collection = db["NombreD'étudiants"]

# Récupérer les documents de la collection
documents = collection.find()

# Fonction pour construire les contextes
def construire_contextes_nombre_etudiants(data):
    contexts = []
    for entry in data:
        annee_de_linscription = entry.get('annee_de_linscription', 'inconnu')
        nationalite_continent = entry.get('nationalite_continent', 'inconnu')
        classe_dage = entry.get('classe_dage', 'inconnu')
        csp_parents = entry.get('csp_parents', 'inconnu')
        sexe = entry.get('sexe', 'inconnu')
        nationalite_francaise_on = entry.get('nationalite_francaise_on', 'inconnu')
        nationalite_pays = entry.get('nationalite_pays', 'inconnu')
        neo_bachelier_on = entry.get('neo_bachelier_on', 'inconnu')
        groupe_de_bac = entry.get('groupe_de_bac', 'inconnu')
        bac_serie = entry.get('bac_serie', 'inconnu')
        bac_mention = entry.get('bac_mention', 'inconnu')
        lieu_du_bac = entry.get('lieu_du_bac', 'inconnu')
        composante = entry.get('composante', 'inconnu')
        neo_entrants_o_n = entry.get('neo_entrants_o_n', 'inconnu')
        cursus_lmd = entry.get('cursus_lmd', 'inconnu')
        niveau = entry.get('niveau', 'inconnu')
        type_de_diplome = entry.get('type_de_diplome', 'inconnu')
        etape = entry.get('etape', 'inconnu')
        diplome_saclay = entry.get('diplome_saclay', 'inconnu')
        regime = entry.get('regime', 'inconnu')
        etudiant_oui_si = entry.get('etudiant_oui_si', 'inconnu')
        redoublement = entry.get('redoublement', 'inconnu')
        nombre_etudiants = entry.get('nombre_etudiants', 'inconnu')

        context = (f"Pour l'année {annee_de_linscription}, {nombre_etudiants} étudiant(s) ont(a) été inscrit(s) en {niveau}, de sexe {sexe}, de nationalité {nationalite_pays}. "
                   f"Ils ont eu un {bac_serie} avec une mention {bac_mention}, provenant du groupe de baccalauréat {groupe_de_bac}. "
                   f"Ils sont inscrits à l'étape {etape}, dans la composante {composante}. "
                   f"Ils sont {etudiant_oui_si} Oui-Si, de régime {regime}, et ne sont pas des redoublants.")
        contexts.append(context)
    return contexts

# Construire les contextes à partir des documents récupérés
contexts_nombre_etudiants = construire_contextes_nombre_etudiants(documents)

# Afficher les contextes pour vérification
for context in contexts_nombre_etudiants:
    print(context)
