from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Sélectionner la base de données
db = client['ProjetChatbot']

# Sélectionner la collection
collection = db["InscriptionsUEVE2019-2021"]

# Récupérer les documents de la collection
documents = collection.find()

# Fonction pour traduire les valeurs 'O' et 'N' en phrases expressives
def traduire_oui_non(valeur):
    if valeur == 'O':
        return "oui"
    elif valeur == 'N':
        return "non"
    else:
        return "inconnu"

# Fonction pour construire les contextes avec des phrases expressives
def construire_contextes_inscriptions_ueve(data):
    contexts = []
    for entry in data:
        context = f"Pour l'année d'inscription {entry.get('annee_de_linscription', 'inconnu')}, "
        context += f"l'étudiant âgé de {entry.get('age_au_1er_octobre', 'inconnu')} ans le 1er octobre "
        context += f"est dans la classe d'âge {entry.get('classe_dage', 'inconnu')}, avec des parents ayant une CSP de "
        context += f"{entry.get('csp_parents', 'inconnu')}. Cet étudiant est de sexe {entry.get('sexe', 'inconnu')}, "
        context += f"de nationalité {entry.get('nationalite_pays', 'inconnu')} (continent {entry.get('nationalite_continent', 'inconnu')}). "
        context += f"Le bac a été obtenu en {entry.get('bac_annee_d_obtention', 'inconnu')}, avec la mention {entry.get('bac_mention', 'inconnu')}, "
        context += f"dans le groupe {entry.get('groupe_de_bac', 'inconnu')} et la série {entry.get('bac_serie', 'inconnu')}. "
        context += f"Le lieu d'obtention du bac est {entry.get('lieu_du_bac', 'inconnu')}. "
        context += f"L'étudiant appartient à la composante {entry.get('composante', 'inconnu')}, est néo-entrant: {traduire_oui_non(entry.get('neo_entrants_o_n', 'inconnu'))}, "
        context += f"en niveau {entry.get('niveau', 'inconnu')} et en étape {entry.get('etape', 'inconnu')}. "
        context += f"Le diplôme visé est un(e) {entry.get('type_de_diplome', 'inconnu')} en {entry.get('diplome', 'inconnu')}, "
        context += f"dans la filière {entry.get('filiere', 'inconnu')}, en régime {entry.get('regime', 'inconnu')}. "
        context += f"Le cursus LMD est {entry.get('cursus_lmd', 'inconnu')}, avec un diplôme COMUE: {entry.get('diplome_comue', 'inconnu')}. "
        context += f"Boursier critères sociaux: {traduire_oui_non(entry.get('boursier_criteres_sociaux_on', 'inconnu'))}, type de bourse: {entry.get('bourse_type', 'inconnu')}, salarié: {traduire_oui_non(entry.get('salarie_on', 'inconnu'))}, "
        context += f"quotité travaillée: {entry.get('salarie_quotite_travaillee', 'inconnu')}. "
        context += f"Domaine de formation: {entry.get('domaine_de_formation', 'inconnu')}, dernier établissement fréquenté: {entry.get('etabliss_dernier_frequente_lib', 'inconnu')} "
        context += f"(type: {entry.get('type_dernier_etab_frequente_lib', 'inconnu')}), préparation bac: {entry.get('bac_etab_preparation_lib', 'inconnu')}. "
        context += f"Validation CVE: {traduire_oui_non(entry.get('temoin_validation_cve', 'inconnu'))}, exonération CVE: {traduire_oui_non(entry.get('temoin_exoneration_cve', 'inconnu'))} "
        context += f"(motif: {entry.get('motif_exoneration_cve', 'inconnu')}). Année N-1: {entry.get('date_annee_n_1', 'inconnu')}, redoublement: {entry.get('redoublement', 'inconnu')}, "
        context += f"typologie selon N-1: {entry.get('typologie_selon_n_1', 'inconnu')}, cumulatif: {entry.get('cumulatif', 'inconnu')}. "
        context += f"Établissement parallèle: {entry.get('lib_etab_parallele', 'inconnu')} (type: {entry.get('type_etab_parallele', 'inconnu')}). "
        context += f"Département: {entry.get('departement', 'inconnu')}, EDS 1ère: {entry.get('bac_1_eds', 'inconnu')}, EDS 2ème: {entry.get('bac_2_eds', 'inconnu')}, "
        context += f"EDS terminal: {entry.get('eds_1_term', 'inconnu')}, EDS terminal 2: {entry.get('eds_term_2', 'inconnu')}, "
        context += f"EDS abandonné: {entry.get('eds_aband', 'inconnu')}, combinaison EDS: {entry.get('combinaison_eds', 'inconnu')}. "
        context += f"Forme géo: {entry.get('forme_geo', 'inconnu')}, Geo point 2D: {entry.get('geo_point_2d', 'inconnu')}."
        contexts.append(context)
    return contexts

# Construire les contextes à partir des documents récupérés
contexts_inscriptions_ueve = construire_contextes_inscriptions_ueve(documents)

# Afficher les contextes pour vérification
for context in contexts_inscriptions_ueve:
    print(context)
