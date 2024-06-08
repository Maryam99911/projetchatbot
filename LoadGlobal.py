import pickle
from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')
# Sélectionner la base de données
db = client['ProjetChatbot']

# Sélectionner la collection
collection = db['aides-financieres-cvec']

# Récupérer les documents de la collection
documents = collection.find()

# Fonction pour construire les contextes
def construirecontextesaidesfinancieres(data):
    contexts = []
    for entry in data:
        annee = entry['annee_civile'].split('-')[0]
        context = (f"En {annee}, il y avait {entry['nb_dossiers_deposes']} dossiers déposés, "
                   f"{entry['nb_dossiers_acceptes']} dossiers acceptés, avec un budget de "
                   f"{entry['budget']} euros et une aide moyenne de {entry['aide_moyenne']} euros.")
        contexts.append(context)
    return contexts

# Construire les contextes à partir des documents récupérés
contexts_aides_financieres = construirecontextesaidesfinancieres(documents)

# Afficher les contextes pour vérification
for context in contexts_aides_financieres:
    print(context)


# Sélectionner la collection
collection = db['AidesNumeriques']

# Récupérer les documents de la collection
documents = collection.find()

# Fonction pour construire les contextes
def construire_contextes_aides_financieres(data):
    contexts = []
    for entry in data:
        annee = entry['annee_civile'].split('-')[0]
        context = (f"En {annee}, il y avait {entry['nb_dossiers_deposes']} dossiers déposés, "
                   f"{entry['nb_dossiers_acceptes']} dossiers acceptés, avec un budget de "
                   f"{entry['budget']} euros et une aide moyenne de {entry['aide_moyenne']} euros "
                   f"pour le type de financement {entry['type']}.")
        contexts.append(context)
    return contexts

# Construire les contextes à partir des documents récupérés
contexts_aides_financieres2 = construire_contextes_aides_financieres(documents)

# Afficher les contextes pour vérification
for context in contexts_aides_financieres:
    print(context)


# Sélectionner la collection
collection = db['associations-etudiantes']

# Récupérer les documents de la collection
documents = collection.find()

# Fonction pour construire les contextes
def construire_contextes_associations(data):
    contexts = []
    for entry in data:
        # Gestion des valeurs None ou manquantes
        code_postal = int(entry['code_postal']) if entry.get('code_postal') is not None else 'inconnu'
        numero_de_voie = int(entry['numero_de_voie']) if entry.get('numero_de_voie') is not None else 'inconnu'
        voie = entry.get('voie', 'voie inconnue')
        site_web = entry.get('site_web', 'pas de site web')
        reseaux_sociaux = entry.get('reseaux_sociaux', 'pas de réseaux sociaux')

        context = (f"L'association {entry['nom']} ({entry['sigle']}) située à {entry['commune']} "
                   f"dans le code postal {code_postal} {voie} {numero_de_voie}, "
                   f"présidée par {entry['president']}, a pour objectif {entry['description']}. "
                   f"Vous pouvez en savoir plus sur leur site web : {site_web} "
                   f"ou les suivre sur leurs réseaux sociaux : {reseaux_sociaux}.")
        contexts.append(context)
    return contexts

# Construire les contextes à partir des documents récupérés
contexts_associations = construire_contextes_associations(documents)

# Afficher les contextes pour vérification
for context in contexts_associations:
    print(context)


# Sélectionner la collection
collection = db["BâtimentsetServicesdel'Universitéd'Evry"]


# Récupérer les documents de la collection
documents = collection.find()


# Fonction pour construire les contextes
def construire_contextes_batiments_services(data):
    contexts = []
    for entry in data:
        adresse = entry['adresse'] if entry['adresse'] is not None else 'adresse inconnue'
        code_postal = entry['code_postal'] if entry['code_postal'] is not None else 'code postal inconnu'
        commune = entry['commune'] if entry['commune'] is not None else 'commune inconnue'
        latitude = entry['latitude'] if entry['latitude'] is not None else 'latitude inconnue'
        longitude = entry['longitude'] if entry['longitude'] is not None else 'longitude inconnue'

        context = (f"Le {entry['type_de_donnee']} {entry['nom']} situé à {adresse} "
                   f"dans le code postal {code_postal} à {commune}, "
                   f"est localisé aux coordonnées ({latitude}, {longitude}).")
        contexts.append(context)
    return contexts


# Construire les contextes à partir des documents récupérés
contexts_batiments_services = construire_contextes_batiments_services(documents)

# Afficher les contextes pour vérification
for context in contexts_batiments_services:
    print(context)


# Sélectionner la collection
collection = db["candidatures-parcoursup2019"]

# Récupérer les documents de la collection
documents = collection.find()

# Fonction pour construire les contextes
def construire_contextes_candidatures_parcoursup(data):
    contexts = []
    for entry in data:
        filiere = entry.get('filiere', 'inconnu')
        nombre_candidatures = entry.get('nombre_candidatures', 'inconnu')

        context = f"La filière '{filiere}' a reçu {nombre_candidatures} candidatures."
        contexts.append(context)
    return contexts

# Construire les contextes à partir des documents récupérés
contexts_candidatures_parcoursup = construire_contextes_candidatures_parcoursup(documents)

# Afficher les contextes pour vérification
for context in contexts_candidatures_parcoursup:
    print(context)


# Sélectionner la collection
collection = db['CaractéristiquesDesEtudiants']

# Récupérer les documents de la collection
documents = collection.find()

def construire_contextes_etudiants(data):
    contexts = []
    for entry in data:
        annee_inscription = entry.get('annee_de_linscription', 'année d\'inscription inconnue')
        genre = entry.get('genre', 'genre inconnu')
        cursus = entry.get('cursus_lmd', 'cursus inconnu')
        regime_inscription = entry.get('regime_d_inscription', 'régime d\'inscription inconnu')
        domaine_formation = entry.get('domaine_de_formation', 'domaine de formation inconnu')
        type_bac_obtenu = entry.get('type_de_bac_obtenu', 'type de baccalauréat inconnu')
        nb_etudiants = entry.get('nombre_d_etudiants', 'nombre d\'étudiants inconnu')
        nb_nouveaux_bacheliers = entry.get('nombre_de_nouveaux_bacheliers', 'nombre de nouveaux bacheliers inconnu')

        context = (f"Pour l'{annee_inscription}, {nb_etudiants} étudiants ont été inscrits, dont "
                   f"{nb_nouveaux_bacheliers} nouveaux bacheliers. Ils sont principalement de genre {genre}, inscrits "
                   f"dans le cursus {cursus}, de régime d'inscription {regime_inscription}, et étudient dans le domaine "
                   f"{domaine_formation}. Le type de baccalauréat obtenu par ces étudiants est {type_bac_obtenu}.")
        contexts.append(context)
    return contexts

# Construire les contextes à partir des documents récupérés
contexts_etudiants = construire_contextes_etudiants(documents)

# Afficher les contextes pour vérification
for context in contexts_etudiants:
    print(context)


# Sélectionner la collection
collection = db["ChiffresClésSurL'universitéD'evry"]


# Récupérer les documents de la collection
documents = collection.find()

def construire_contextes_chiffres_cles(data):
    contexts = []
    for entry in data:
        theme = entry.get('theme', 'thème inconnu')
        chiffres = entry.get('chiffres', 'chiffres inconnus')
        variables = entry.get('variables', 'variables inconnues')

        context = f"Pour le thème '{theme}', il y a {chiffres} {variables}."
        contexts.append(context)
    return contexts

# Construire les contextes à partir des documents récupérés
contexts_chiffres_cles = construire_contextes_chiffres_cles(documents)

# Afficher les contextes pour vérification
for context in contexts_chiffres_cles:
    print(context)


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
contexts_consommation_electricite2 = construire_contextes_consommation_electricite(documents)

# Afficher les contextes pour vérification
for context in contexts_consommation_electricite:
    print(context)

# Sélectionner la collection
collection = db["ConsommationElectriqueParJour"]

# Récupérer les documents de la collection
documents = collection.find()


def construire_contextes_consommation_electrique(data):
    contexts = []
    for entry in data:
        location = entry.get('location', 'localisation inconnue')
        batiments = ", ".join(
            [f"{key.replace('_', ' ').title()}: {value}" for key, value in entry.items() if key.startswith('batiment')])

        context = f"Le {location}, la consommation électrique par jour pour les bâtiments est : {batiments}."
        contexts.append(context)
    return contexts


# Construire les contextes à partir des documents récupérés
contexts_consommation_electrique = construire_contextes_consommation_electrique(documents)

# Afficher les contextes pour vérification
for context in contexts_consommation_electrique:
    print(context)


# Sélectionner la collection
collection = db["ConsommationenEau"]

# Récupérer les documents de la collection
documents = collection.find()

def construire_contextes_consommation_eau(data):
    contexts = []
    for entry in data:
        location = entry.get('location', 'date inconnue')
        premiers_cycles = entry.get('batiment_premiers_cycles', 'donnée inconnue')
        iut_romero = entry.get('batiment_iut_romero', 'donnée inconnue')
        bibliotheque_universitaire = entry.get('batiment_bibliotheque_universitaire', 'donnée inconnue')
        facteur_cheval = entry.get('batiment_facteur_cheval', 'donnée inconnue')
        ibgbi = entry.get('batiment_ibgbi', 'donnée inconnue')
        ile_de_france = entry.get('batiment_ile_de_france', 'donnée inconnue')
        maupertuis = entry.get('batiment_maupertuis', 'donnée inconnue')
        iut_romero0 = entry.get('batiment_iut_romero0', 'donnée inconnue')

        context = (f"Pour la date {location}, la consommation d'eau est la suivante :\n"
                   f"- Premiers cycles : {premiers_cycles}\n"
                   f"- IUT Roméro : {iut_romero}\n"
                   f"- Bibliothèque Universitaire : {bibliotheque_universitaire}\n"
                   f"- Facteur Cheval : {facteur_cheval}\n"
                   f"- IBGBI : {ibgbi}\n"
                   f"- Île de France : {ile_de_france}\n"
                   f"- Maupertuis : {maupertuis}\n"
                   f"- IUT Roméro 0 : {iut_romero0}")

        contexts.append(context)
    return contexts

# Construire les contextes à partir des documents récupérés
contexts_consommation_eau = construire_contextes_consommation_eau(documents)

# Afficher les contextes pour vérification
for context in contexts_consommation_eau:
    print(context)


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

# Sélectionner la collection
collection = db["EcartRemuneration2022-DécompositionDesEcarts"]

# Récupérer les documents de la collection
documents = collection.find()

# Fonction pour construire les contextes
def construire_contextes_ecart_remuneration(data):
    contexts = []
    for entry in data:
        titulaire_ou_contractuel = entry.get('titulaire_ou_contractuel', 'inconnu')
        categorie = entry.get('categorie', 'inconnue')
        effet_demographique = entry.get('effet_demographique_au_sein_des_corps_dont_sur_primes', 'inconnu')
        sur_remuneration_temps_partiel = entry.get('sur_remuneration_temps_partiel_80_ou_90', 'inconnue')
        temps_ou_aux_cycles_de_travail = entry.get('temps_ou_aux_cycles_de_travail', 'inconnue')
        geographie_et_aux_mobilites = entry.get('geographie_et_aux_mobilites_non_forcees', 'inconnue')
        resultats_performance = entry.get('resultats_performance_engagement_professionnel', 'inconnue')
        remunerations_accessoires = entry.get('remunerations_accessoires', 'inconnue')
        fonctions_sujetions_indexees = entry.get('fonctions_sujetions_indexees_sur_le_traitement', 'inconnue')
        fonctions_sujetions_non_indexees = entry.get('fonctions_sujetions_non_indexees_sur_le_traitement', 'inconnue')
        restructurations_ou_mobilites = entry.get('restructurations_ou_mobilites_forcees', 'inconnue')
        autres_primes_et_ecarts_residuels = entry.get('autres_primes_et_ecarts_residuels_sur_traitement', 'inconnue')

        context = (f"Pour les {categorie} {titulaire_ou_contractuel}, "
                   f"l'effet démographique est de {effet_demographique}, "
                   f"la sur-rémunération en temps partiel est de {sur_remuneration_temps_partiel}, "
                   f"l'effet géographique et aux mobilités est de {geographie_et_aux_mobilites}, "
                   f"les résultats de performance et engagement professionnel sont de {resultats_performance}, "
                   f"les rémunérations accessoires sont de {remunerations_accessoires}, "
                   f"les fonctions sujetions indexées sur le traitement sont de {fonctions_sujetions_indexees}, "
                   f"les fonctions sujetions non indexées sur le traitement sont de {fonctions_sujetions_non_indexees}, "
                   f"les restructurations ou mobilites forcees sont de {restructurations_ou_mobilites}, "
                   f"et les autres primes et écarts résiduels sur traitement sont de {autres_primes_et_ecarts_residuels}.")
        contexts.append(context)
    return contexts

# Construire les contextes à partir des documents récupérés
contexts_ecart_remuneration = construire_contextes_ecart_remuneration(documents)

# Afficher les contextes pour vérification
for context in contexts_ecart_remuneration:
    print(context)

# Sélectionner la collection
collection = db["EcartRemuneration2022-ParCorps"]

# Récupérer les documents de la collection
documents = collection.find()

# Fonction pour construire les contextes
def construire_contextes_ecart_remuneration(data):
    contexts = []
    for entry in data:
        liste_des_corps = entry.get('liste_des_corps', 'liste des corps inconnue')
        categorie = entry.get('categorie', 'catégorie inconnue')
        typeContractuelTitulaire = entry.get('titulaire_ou_contractuel', 'Type inconnu')
        remuneration_homme = entry.get('remuneration_mensuelle_moyenne_par_eqtp_homme', 'remunération homme inconnue')
        remuneration_femme = entry.get('remuneration_mensuelle_moyenne_par_eqtp_femme', 'remunération femme inconnue')
        ecart_remuneration = entry.get('ecarts_remuneration_f_h', 'écart de rémunération inconnu')
        effectifs_physiques_hommes = entry.get('effectifs_physiques_hommes', 'effectifs physiques hommes inconnus')
        effectifs_physiques_femmes = entry.get('effectifs_physiques_femmes', 'effectifs physiques femmes inconnus')
        etpt_hommes = entry.get('etpt_hommes', 'ETPT hommes inconnu')
        etpt_femmes = entry.get('etpt_femmes', 'ETPT femmes inconnu')
        taux_moyen_de_temps_partiel_hommes = entry.get('taux_moyen_de_temps_partiel_hommes', 'taux moyen de temps partiel hommes inconnu')
        taux_moyen_de_temps_partiel_femmes = entry.get('taux_moyen_de_temps_partiel_femmes', 'taux moyen de temps partiel femmes inconnu')
        indicateur_mixite_salaire = entry.get('indicateur_mixite_salaire', 'indicateur de mixité salariale inconnu')
        indicateur_mixite_emploi = entry.get('indicateur_mixite_emploi', 'indicateur de mixité emploi inconnu')
        indicateur_qualite_tib = entry.get('indicateur_qualite_tib', 'indicateur de qualité TIB inconnu')
        effect_demographique_du_corps = entry.get('effet_demographique_du_corps', 'effet démographique du corps inconnu')
        effet_primes_a_c_g_e_identique_lie_a_sur_remuneration_temps_partiel_80_ou_90 = entry.get('effet_primes_a_c_g_e_identique_lie_a_sur_remuneration_temps_partiel_80_ou_90', 'effet primes ACGE identique lié à sur rémunération temps partiel 80 ou 90 inconnu')
        effet_primes_a_c_g_e_identique_lie_a_temps_ou_aux_cycles_de_travail = entry.get('effet_primes_a_c_g_e_identique_lie_a_temps_ou_aux_cycles_de_travail', 'effet primes ACGE identique lié à temps ou aux cycles de travail inconnu')
        effet_primes_a_c_g_e_identique_lie_a_geographie_et_aux_mobilites_non_forcees = entry.get('effet_primes_a_c_g_e_identique_lie_a_geographie_et_aux_mobilites_non_forcees', 'effet primes ACGE identique lié à géographie et aux mobilités non forcées inconnu')
        effet_primes_a_c_g_e_identique_lie_a_resultats_performance_engagement_professionnel = entry.get('effet_primes_a_c_g_e_identique_lie_a_resultats_performance_engagement_professionnel', 'effet primes ACGE identique lié à résultats performance engagement professionnel inconnu')
        effet_primes_a_c_g_e_identique_lie_a_remunerations_accessoires = entry.get('effet_primes_a_c_g_e_identique_lie_a_remunerations_accessoires', 'effet primes ACGE identique lié à rémunérations accessoires inconnu')
        effet_primes_a_c_g_e_identique_lie_a_fonctions_sujetions_indexees_sur_le_traitement = entry.get('effet_primes_a_c_g_e_identique_lie_a_fonctions_sujetions_indexees_sur_le_traitement', 'effet primes ACGE identique lié à fonctions sujétions indexées sur le traitement inconnu')
        effet_primes_a_c_g_e_identique_lie_a_fonctions_sujetions_non_indexees_sur_le_traitement = entry.get('effet_primes_a_c_g_e_identique_lie_a_fonctions_sujetions_non_indexees_sur_le_traitement', 'effet primes ACGE identique lié à fonctions sujétions non indexées sur le traitement inconnu')
        effet_primes_a_c_g_e_identique_lie_a_restructurations_ou_mobilites_forcees = entry.get('effet_primes_a_c_g_e_identique_lie_a_restructurations_ou_mobilites_forcees', 'effet primes ACGE identique lié à restructurations ou mobilités forcées inconnu')
        effet_primes_a_c_g_e_identique_lie_a_autres_primes_et_ecarts_residuels_sur_traitement = entry.get('effet_primes_a_c_g_e_identique_lie_a_autres_primes_et_ecarts_residuels_sur_traitement', 'effet primes ACGE identique lié à autres primes et écarts résiduels sur traitement inconnu')
        effet_primes_h_a_c_g_e_identique_lie_a_sur_remuneration_temps_partiel_80_ou_90 = entry.get('effet_primes_h_a_c_g_e_identique_lie_a_sur_remuneration_temps_partiel_80_ou_90','effet primes HACGE identique lié à sur rémunération temps partiel 80 ou 90 inconnu')
        effet_primes_h_a_c_g_e_identique_lie_a_temps_ou_aux_cycles_de_travail = entry.get(
            'effet_primes_h_a_c_g_e_identique_lie_a_temps_ou_aux_cycles_de_travail',
            'effet primes HACGE identique lié à temps ou aux cycles de travail inconnu')
        effet_primes_h_a_c_g_e_identique_lie_a_geographie_et_aux_mobilites_non_forcees = entry.get(
            'effet_primes_h_a_c_g_e_identique_lie_a_geographie_et_aux_mobilites_non_forcees',
            'effet primes HACGE identique lié à géographie et aux mobilités non forcées inconnu')
        effet_primes_h_a_c_g_e_identique_lie_a_resultats_performance_engagement_professionnel = entry.get(
            'effet_primes_h_a_c_g_e_identique_lie_a_resultats_performance_engagement_professionnel',
            'effet primes HACGE identique lié à résultats performance engagement professionnel inconnu')
        effet_primes_h_a_c_g_e_identique_lie_a_remunerations_accessoires = entry.get(
            'effet_primes_h_a_c_g_e_identique_lie_a_remunerations_accessoires',
            'effet primes HACGE identique lié à rémunérations accessoires inconnu')
        effet_primes_h_a_c_g_e_identique_lie_a_fonctions_sujetions_indexees_sur_le_traitement = entry.get(
            'effet_primes_h_a_c_g_e_identique_lie_a_fonctions_sujetions_indexees_sur_le_traitement',
            'effet primes HACGE identique lié à fonctions sujétions indexées sur le traitement inconnu')
        effet_primes_h_a_c_g_e_identique_lie_a_fonctions_sujetions_non_indexees_sur_le_traitement = entry.get(
            'effet_primes_h_a_c_g_e_identique_lie_a_fonctions_sujetions_non_indexees_sur_le_traitement',
            'effet primes HACGE identique lié à fonctions sujétions non indexées sur le traitement inconnu')
        effet_primes_h_a_c_g_e_identique_lie_a_restructurations_ou_mobilites_forcees = entry.get(
            'effet_primes_h_a_c_g_e_identique_lie_a_restructurations_ou_mobilites_forcees',
            'effet primes HACGE identique lié à restructurations ou mobilités forcées inconnu')
        effet_primes_h_a_c_g_e_identique_lie_a_autres_primes_et_ecarts_residuels_sur_traitement = entry.get(
            'effet_primes_h_a_c_g_e_identique_lie_a_autres_primes_et_ecarts_residuels_sur_traitement',
            'effet primes HACGE identique lié à autres primes et écarts résiduels sur traitement inconnu')
        context = (
            f"Dans le corps {liste_des_corps}, de catégorie {categorie}, il s'agit d'un {typeContractuelTitulaire}, la Rémunération moyenne mensuelle par EQTP (homme) est de {remuneration_homme}, "
            f"la Rémunération moyenne mensuelle par EQTP (femme) est de {remuneration_femme}, l'Écart de rémunération entre hommes et femmes est de {ecart_remuneration}, "
            f"les Effectifs physiques des hommes sont {effectifs_physiques_hommes}, les Effectifs physiques des femmes sont {effectifs_physiques_femmes}, "
            f"les ETPT (hommes) sont de {etpt_hommes}, les ETPT (femmes) sont de {etpt_femmes}, les Taux moyen de temps partiel pour les hommes sont de {taux_moyen_de_temps_partiel_hommes}, "
            f"les Taux moyen de temps partiel pour les femmes sont de {taux_moyen_de_temps_partiel_femmes}, l'Indicateur de mixité salariale est de {indicateur_mixite_salaire}, "
            f"l'Indicateur de mixité emploi est de {indicateur_mixite_emploi}, l'Indicateur de qualité TIB est de {indicateur_qualite_tib}, l'Effet démographique du corps est de {effect_demographique_du_corps}, "
            f"l'Effet primes ACGE identique lié à sur rémunération temps partiel 80 ou 90 est de {effet_primes_a_c_g_e_identique_lie_a_sur_remuneration_temps_partiel_80_ou_90}, "
            f"l'Effet primes ACGE identique lié à temps ou aux cycles de travail est de {effet_primes_a_c_g_e_identique_lie_a_temps_ou_aux_cycles_de_travail}, "
            f"l'Effet primes ACGE identique lié à géographie et aux mobilités non forcées est de {effet_primes_a_c_g_e_identique_lie_a_geographie_et_aux_mobilites_non_forcees}, "
            f"l'Effet primes ACGE identique lié à résultats performance engagement professionnel est de {effet_primes_a_c_g_e_identique_lie_a_resultats_performance_engagement_professionnel}, "
            f"l'Effet primes ACGE identique lié à rémunérations accessoires est de {effet_primes_a_c_g_e_identique_lie_a_remunerations_accessoires}, "
            f"l'Effet primes ACGE identique lié à fonctions sujétions indexées sur le traitement est de {effet_primes_a_c_g_e_identique_lie_a_fonctions_sujetions_indexees_sur_le_traitement}, "
            f"l'Effet primes ACGE identique lié à fonctions sujétions non indexées sur le traitement est de {effet_primes_a_c_g_e_identique_lie_a_fonctions_sujetions_non_indexees_sur_le_traitement}, "
            f"l'Effet primes ACGE identique lié à restructurations ou mobilités forcées est de {effet_primes_a_c_g_e_identique_lie_a_restructurations_ou_mobilites_forcees}, "
            f"l'Effet primes ACGE identique lié à autres primes et écarts résiduels sur traitement est de {effet_primes_a_c_g_e_identique_lie_a_autres_primes_et_ecarts_residuels_sur_traitement}, "
            f"l'Effet primes HACGE identique lié à sur rémunération temps partiel 80 ou 90 est de {effet_primes_h_a_c_g_e_identique_lie_a_sur_remuneration_temps_partiel_80_ou_90}, "
            f"l'Effet primes HACGE identique lié à temps ou aux cycles de travail est de {effet_primes_h_a_c_g_e_identique_lie_a_temps_ou_aux_cycles_de_travail}, "
            f"l'Effet primes HACGE identique lié à géographie et aux mobilités non forcées est de {effet_primes_h_a_c_g_e_identique_lie_a_geographie_et_aux_mobilites_non_forcees}, "
            f"l'Effet primes HACGE identique lié à résultats performance engagement professionnel est de {effet_primes_h_a_c_g_e_identique_lie_a_resultats_performance_engagement_professionnel}, "
            f"l'Effet primes HACGE identique lié à rémunérations accessoires est de {effet_primes_h_a_c_g_e_identique_lie_a_remunerations_accessoires}, "
            f"l'Effet primes HACGE identique lié à fonctions sujétions indexées sur le traitement est de {effet_primes_h_a_c_g_e_identique_lie_a_fonctions_sujetions_indexees_sur_le_traitement}, "
            f"l'Effet primes HACGE identique lié à fonctions sujétions non indexées sur le traitement est de {effet_primes_h_a_c_g_e_identique_lie_a_fonctions_sujetions_non_indexees_sur_le_traitement}, "
            f"l'Effet primes HACGE identique lié à restructurations ou mobilités forcées est de {effet_primes_h_a_c_g_e_identique_lie_a_restructurations_ou_mobilites_forcees}, "
            f"l'effet_primes_h_a_c_g_e_identique_lie_a_autres_primes_et_ecarts_residuels_sur_traitement est de {effet_primes_h_a_c_g_e_identique_lie_a_autres_primes_et_ecarts_residuels_sur_traitement}.")
        contexts.append(context)
    return contexts


# Construire les contextes à partir des documents récupérés
contexts_ecart_remuneration_par_corps = construire_contextes_ecart_remuneration(documents)

# Afficher les contextes pour vérification
for context in contexts_ecart_remuneration_par_corps:
    print(context)



# Sélectionner la collection
collection = db["EcartRemuneration2022-RésultatsGlobaux"]

# Récupérer les documents de la collection
documents = collection.find()

# Fonction pour construire les contextes
def construire_contextes_resultats_globaux(data):
    contexts = []
    for entry in data:
        titulaire_ou_contractuel = entry.get('titulaire_ou_contractuel', 'inconnu')
        nombre_de_corps_pris_en_compte = entry.get('nombre_de_corps_pris_en_compte', 'inconnu')
        emploi_annuel_moyen_hommes_effectifs_annuels = entry.get('emploi_annuel_moyen_hommes_effectifs_annuels', 'inconnu')
        emploi_annuel_moyen_femmes_effectifs_annuels = entry.get('emploi_annuel_moyen_femmes_effectifs_annuels', 'inconnu')
        part_des_femmes_effectifs_annuels = entry.get('part_des_femmes_effectifs_annuels', 'inconnu')
        emploi_annuel_moyen_hommes_equivalents_temps_plein_employes = entry.get('emploi_annuel_moyen_hommes_equivalents_temps_plein_employes', 'inconnu')
        emploi_annuel_moyen_femmes_equivalents_temps_plein_employes = entry.get('emploi_annuel_moyen_femmes_equivalents_temps_plein_employes', 'inconnu')
        part_des_femmes_equivalents_temps_plein_employes = entry.get('part_des_femmes_equivalents_temps_plein_employes', 'inconnu')
        taux_moyen_de_temps_partiel_hommes = entry.get('taux_moyen_de_temps_partiel_hommes', 'inconnu')
        taux_moyen_de_temps_partiel_femmes = entry.get('taux_moyen_de_temps_partiel_femmes', 'inconnu')
        taux_moyen_de_temps_partiel_total = entry.get('taux_moyen_de_temps_partiel_total', 'inconnu')
        remuneration_mensuelle_moyenne_en_eur_non_redressee_du_temps_partiel_et_de_la_presence_partielle_dan = entry.get('remuneration_mensuelle_moyenne_en_eur_non_redressee_du_temps_partiel_et_de_la_presence_partielle_dan', 'inconnu')
        remuneration_mensuelle_moyenne_en_eur_non_redressee_du_temps_partiel_et_de_la_presence_partielle_da0 = entry.get('remuneration_mensuelle_moyenne_en_eur_non_redressee_du_temps_partiel_et_de_la_presence_partielle_da0', 'inconnu')
        remuneration_mensuelle_moyenne_en_eur_non_redressee_du_temps_partiel_et_de_la_presence_partielle_da1 = entry.get('remuneration_mensuelle_moyenne_en_eur_non_redressee_du_temps_partiel_et_de_la_presence_partielle_da1', 'inconnu')
        remuneration_mensuelle_moyenne_en_eur_non_redressee_du_temps_partiel_et_de_la_presence_partielle_da2 = entry.get('remuneration_mensuelle_moyenne_en_eur_non_redressee_du_temps_partiel_et_de_la_presence_partielle_da2', 'inconnu')
        remuneration_mensuelle_moyenne_en_eur_par_equivalent_temps_plein_hommes = entry.get('remuneration_mensuelle_moyenne_en_eur_par_equivalent_temps_plein_hommes', 'inconnu')
        remuneration_mensuelle_moyenne_en_eur_par_equivalent_temps_plein_femmes = entry.get('remuneration_mensuelle_moyenne_en_eur_par_equivalent_temps_plein_femmes', 'inconnu')
        remuneration_mensuelle_moyenne_en_eur_par_equivalent_temps_plein_ecart_en_eur_mois = entry.get('remuneration_mensuelle_moyenne_en_eur_par_equivalent_temps_plein_ecart_en_eur_mois', 'inconnu')
        remuneration_mensuelle_moyenne_en_eur_par_equivalent_temps_plein_ecart_par_genre_f_h_h = entry.get('remuneration_mensuelle_moyenne_en_eur_par_equivalent_temps_plein_ecart_par_genre_f_h_h', 'inconnu')

        context = (f"Pour les {titulaire_ou_contractuel}, le nombre de corps pris en compte est de {nombre_de_corps_pris_en_compte}, "
                   f"l'emploi annuel moyen des hommes (effectifs annuels) est de {emploi_annuel_moyen_hommes_effectifs_annuels}, "
                   f"l'emploi annuel moyen des femmes (effectifs annuels) est de {emploi_annuel_moyen_femmes_effectifs_annuels}, "
                   f"la part des femmes (effectifs annuels) est de {part_des_femmes_effectifs_annuels}%, "
                   f"l'emploi annuel moyen des hommes (équivalents temps plein employés) est de {emploi_annuel_moyen_hommes_equivalents_temps_plein_employes}, "
                   f"l'emploi annuel moyen des femmes (équivalents temps plein employés) est de {emploi_annuel_moyen_femmes_equivalents_temps_plein_employes}, "
                   f"la part des femmes (équivalents temps plein employés) est de {part_des_femmes_equivalents_temps_plein_employes}%, "
                   f"le taux moyen de temps partiel des hommes est de {taux_moyen_de_temps_partiel_hommes}%, "
                   f"le taux moyen de temps partiel des femmes est de {taux_moyen_de_temps_partiel_femmes}%, "
                   f"le taux moyen de temps partiel total est de {taux_moyen_de_temps_partiel_total}%, "
                   f"la rémunération mensuelle moyenne en EUR non redressée du temps partiel et de la présence partielle des hommes est de {remuneration_mensuelle_moyenne_en_eur_non_redressee_du_temps_partiel_et_de_la_presence_partielle_dan}€, "
                   f"la rémunération mensuelle moyenne en EUR non redressée du temps partiel et de la présence partielle des femmes est de {remuneration_mensuelle_moyenne_en_eur_non_redressee_du_temps_partiel_et_de_la_presence_partielle_da0}€, "
                   f"la différence de rémunération mensuelle moyenne en EUR non redressée du temps partiel et de la présence partielle entre hommes et femmes est de {remuneration_mensuelle_moyenne_en_eur_non_redressee_du_temps_partiel_et_de_la_presence_partielle_da1}€, "
                   f"le pourcentage de différence de rémunération mensuelle moyenne en EUR non redressée du temps partiel et de la présence partielle entre hommes et femmes est de {remuneration_mensuelle_moyenne_en_eur_non_redressee_du_temps_partiel_et_de_la_presence_partielle_da2}%, "
                   f"la rémunération mensuelle moyenne en EUR par équivalent temps plein des hommes est de {remuneration_mensuelle_moyenne_en_eur_par_equivalent_temps_plein_hommes}€, "
                   f"la rémunération mensuelle moyenne en EUR par équivalent temps plein des femmes est de {remuneration_mensuelle_moyenne_en_eur_par_equivalent_temps_plein_femmes}€, "
                   f"la différence de rémunération mensuelle moyenne en EUR par équivalent temps plein entre hommes et femmes est de {remuneration_mensuelle_moyenne_en_eur_par_equivalent_temps_plein_ecart_en_eur_mois}€, "
                   f"le pourcentage de différence de rémunération mensuelle moyenne en EUR par équivalent temps plein entre hommes et femmes est de {remuneration_mensuelle_moyenne_en_eur_par_equivalent_temps_plein_ecart_par_genre_f_h_h}%.")
        contexts.append(context)
    return contexts

# Construire les contextes à partir des documents récupérés
contexts_resultats_globaux = construire_contextes_resultats_globaux(documents)

# Afficher les contextes pour vérification
for context in contexts_resultats_globaux:
    print(context)


# Sélectionner la collection
collection = db["EcartRemuneration2022-SyntheseScores"]

# Récupérer les documents de la collection
documents = collection.find()

# Fonction pour construire les contextes
def construire_contextes_synthese_scores(data):
    contexts = []
    for entry in data:
        indicateurs = entry.get('indicateurs', 'inconnu')
        note_maximale_initiale = entry.get('note_maximale_initiale', 'inconnu')
        score_initial_de_l_ep = entry.get('score_initial_de_l_ep', 'inconnu')

        context = (f"Pour l'indicateur '{indicateurs}', la note maximale initiale est de {note_maximale_initiale}, "
                   f"et le score initial de l'EP est de {score_initial_de_l_ep}.")
        contexts.append(context)
    return contexts

# Construire les contextes à partir des documents récupérés
contexts_synthese_scores = construire_contextes_synthese_scores(documents)

# Afficher les contextes pour vérification
for context in contexts_synthese_scores:
    print(context)


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
contexts_ecart_remuneration_hautes = construire_contextes_ecart_remuneration(documents)

# Afficher les contextes pour vérification
for context in contexts_ecart_remuneration:
    print(context)


# Sélectionner la collection
collection = db["EvolutionInscriptionsSur14Ans"]

# Récupérer les documents de la collection
documents = collection.find()

# Fonction pour construire les contextes
def construire_contextes_evolution_inscriptions(data):
    contexts = []
    for entry in data:
        annee_universitaire = entry.get('annee_universitaire', 'inconnu')
        cursus_l = entry.get('cursus_l', 'inconnu')
        cursus_m = entry.get('cursus_m', 'inconnu')
        cursus_d = entry.get('cursus_d', 'inconnu')
        nombre_d_etudiants = entry.get('nombre_d_etudiants', 'inconnu')
        nombre_neobacheliers = entry.get('nombre_neobacheliers', 'inconnu')
        nombre_de_neorentrants = entry.get('nombre_de_neorentrants', 'inconnu')

        context = (f"Pour l'année universitaire {annee_universitaire}, le nombre d'étudiants en cursus L est de {cursus_l}, "
                   f"en cursus M est de {cursus_m}, et en cursus D est de {cursus_d}. "
                   f"Le nombre total d'étudiants est de {nombre_d_etudiants}, "
                   f"avec {nombre_neobacheliers} néobacheliers et {nombre_de_neorentrants} néorentrants.")
        contexts.append(context)
    return contexts

# Construire les contextes à partir des documents récupérés
contexts_evolution_inscriptions = construire_contextes_evolution_inscriptions(documents)

# Afficher les contextes pour vérification
for context in contexts_evolution_inscriptions:
    print(context)


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


# Sélectionner la collection
collection = db["NombreD'inscritsParBac"]

# Récupérer les documents de la collection
documents = collection.find()

# Fonction pour construire les contextes
def construire_contextes_nombre_inscrits_par_bac(data):
    contexts = []
    for entry in data:
        annee_de_linscription = entry.get('annee_de_linscription', 'inconnu')
        groupe_de_bac = entry.get('groupe_de_bac', 'inconnu')
        bac_serie = entry.get('bac_serie', 'inconnu')
        niveau = entry.get('niveau', 'inconnu')
        somme_de_nombre_etudiants = entry.get('somme_de_nombre_etudiants', 'inconnu')

        context = (f"Pour l'année {annee_de_linscription}, {somme_de_nombre_etudiants} étudiants ont été inscrits en {niveau} ayant passé le bac série {bac_serie} du groupe {groupe_de_bac}.")
        contexts.append(context)
    return contexts

# Construire les contextes à partir des documents récupérés
contexts_nombre_inscrits_par_bac = construire_contextes_nombre_inscrits_par_bac(documents)

# Afficher les contextes pour vérification
for context in contexts_nombre_inscrits_par_bac:
    print(context)

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

collection = db["NombreInscritsParCursus"]

# Récupérer les documents de la collection
documents = collection.find()

# Fonction pour construire les contextes
def construire_contextes_nombre_inscrits_par_cursus(data):
    contexts = []
    for entry in data:
        annee_de_linscription = entry.get('annee_de_linscription', 'inconnu')
        cursus_lmd = entry.get('cursus_lmd', 'inconnu')
        niveau = entry.get('niveau', 'inconnu')
        somme_nombre_etudiants = entry.get('somme_nombre_etudiants', 'inconnu')

        context = (f"Pour l'année {annee_de_linscription}, {somme_nombre_etudiants} étudiant(s) ont été inscrit(s) en {niveau}, dans le cursus {cursus_lmd}.")
        contexts.append(context)
    return contexts

# Construire les contextes à partir des documents récupérés
contexts_nombre_inscrits_par_cursus = construire_contextes_nombre_inscrits_par_cursus(documents)

# Afficher les contextes pour vérification
for context in contexts_nombre_inscrits_par_cursus:
    print(context)

# Sélectionner la collection
collection = db["PointsDeRestauration"]

# Récupérer les documents de la collection
documents = collection.find()

# Fonction pour construire les contextes
def construire_contextes_points_de_restauration(data):
    contexts = []
    for entry in data:
        site = entry.get('site', 'inconnu')
        restauration = entry.get('restauration', 'inconnu')
        adresse = entry.get('adresse', 'inconnu')
        cp = entry.get('cp', 'inconnu')
        ville = entry.get('ville', 'inconnu')
        poi = entry.get('poi', 'inconnu')

        context = (f"Au {site}, se trouve le restaurant {restauration}, situé à l'adresse {adresse}, {cp} {ville}. "
                   f"Les coordonnées GPS sont {poi['lat']}, {poi['lon']}.")
        contexts.append(context)
    return contexts

# Construire les contextes à partir des documents récupérés
contexts_points_de_restauration = construire_contextes_points_de_restauration(documents)

# Afficher les contextes pour vérification
for context in contexts_points_de_restauration:
    print(context)

collection = db["ProjetsCVEC"]

# Récupérer les documents de la collection
documents = collection.find()

# Fonction pour construire les contextes
def construire_contextes_projets_cvec(data):
    contexts = []
    for entry in data:
        thematique = entry.get('thematique', 'inconnu')
        date = entry.get('date', 'inconnu')
        nom = entry.get('nom', 'inconnu')
        objectifs = entry.get('objectifs', 'inconnu')
        localisation = entry.get('localisation', 'inconnu')

        context = (f"Le projet '{nom}' de thématique '{thematique}' a été initié le {date}. "
                   f"Ses objectifs sont : {objectifs}. ")
        if localisation:
            context += f"Il se situe à l'adresse : {localisation}."
        else:
            context += "La localisation n'est pas spécifiée pour le moment."
        contexts.append(context)
    return contexts

# Construire les contextes à partir des documents récupérés
contexts_projets_cvec = construire_contextes_projets_cvec(documents)

# Afficher les contextes pour vérification
for context in contexts_projets_cvec:
    print(context)


# Sélectionner la collection
collection = db["RéparationVélosGPS"]

# Récupérer les documents de la collection
documents = collection.find()

# Fonction pour construire les contextes
def construire_contextes_reparation_velos_gps(data):
    contexts = []
    for entry in data:
        etablissement = entry.get('etablissement', 'inconnu')
        adresse = entry.get('adresse', 'inconnu')
        code_insee = entry.get('code_insee', 'inconnu')
        commune = entry.get('commune', 'inconnu')
        telephone = entry.get('telephone', 'inconnu')
        site_web = entry.get('site_web', 'inconnu')
        complement = entry.get('complement', 'inconnu')
        geopoint = entry.get('geopoint', 'inconnu')

        context = (f"L'établissement '{etablissement}' propose des services de réparation de vélos. "
                   f"Il est situé à l'adresse : {adresse}, {code_insee} {commune}. ")
        if complement:
            context += f"{complement}. "
        context += f"Vous pouvez les contacter au {telephone} ou visiter leur site web : {site_web}. "
        if geopoint:
            context += f"Les coordonnées GPS sont {geopoint['lat']}, {geopoint['lon']}."
        contexts.append(context)
    return contexts

# Construire les contextes à partir des documents récupérés
contexts_reparation_velos_gps = construire_contextes_reparation_velos_gps(documents)

# Afficher les contextes pour vérification
for context in contexts_reparation_velos_gps:
    print(context)


# Sélectionner la collection
collection = db["TauxDeRéussite"]

# Récupérer les documents de la collection
documents = collection.find()

# Fonction pour construire les contextes
def construire_contextes_taux_de_reussite(data):
    contexts = []
    for entry in data:
        domaine = entry.get('domaine', 'inconnu')
        etape = entry.get('etape', 'inconnu')
        annee_de_l_inscription = entry.get('annee_de_l_inscription', 'inconnu')
        taux_de_reussite = entry.get('taux_de_reussite0', 'inconnu')

        context = (f"Dans le domaine '{domaine}', pour l'étape '{etape}' et l'année d'inscription '{annee_de_l_inscription}', "
                   f"le taux de réussite est de {taux_de_reussite}%.")
        contexts.append(context)
    return contexts

# Construire les contextes à partir des documents récupérés
contexts_taux_de_reussite = construire_contextes_taux_de_reussite(documents)

# Afficher les contextes pour vérification
for context in contexts_taux_de_reussite:
    print(context)

# Rassembler les contextes dans un dictionnaire
contexts_dict = {
    "aides_financieres": contexts_aides_financieres,
    "aides_numeriques": contexts_aides_financieres2,
    "associations_etudiantes": contexts_associations,
    "batiments_services": contexts_batiments_services,
    "candidatures_parcoursup": contexts_candidatures_parcoursup,
    "etudiants": contexts_etudiants,
    "chiffres_cles": contexts_chiffres_cles,
    "consommation_chauffage": contexts_consommation_chauffage,
    "consommation_electricite": contexts_consommation_electricite,
    "consommation_electricite_jour": contexts_consommation_electricite2,
    "consommation_electrique": contexts_consommation_electrique,
    "consommation_eau": contexts_consommation_eau,
    "courbe_charge": contexts_courbe_charge,
    "ecart_remuneration_decomposition": contexts_ecart_remuneration,
    "ecart_remuneration_corps": contexts_ecart_remuneration_par_corps,
    "resultats_globaux": contexts_resultats_globaux,
    "synthese_scores": contexts_synthese_scores,
    "10_plus_hautes_remuneration": contexts_ecart_remuneration_hautes,
    "evolution_inscriptions": contexts_evolution_inscriptions,
    "etablissements_scolaires": contexts_etablissements_scolaires,
    "inscriptions_depuis_2015": contexts_inscriptions_depuis_2015,
    "inscriptions_ueve": contexts_inscriptions_ueve,
    "localisation_distributeurs": contexts_localisation_distributeurs,
    "nombre_etudiants": contexts_nombre_etudiants,
    "nombre_inscrits_par_bac": contexts_nombre_inscrits_par_bac,
    "nombre_inscrits_par_cursus": contexts_nombre_inscrits_par_cursus,
    "points_de_restauration": contexts_points_de_restauration,
    "projets_cvec": contexts_projets_cvec,
    "reparation_velos_gps": contexts_reparation_velos_gps,
    "taux_de_reussite": contexts_taux_de_reussite
}

for key, contexts in contexts_dict.items():
    print(f"\nContexte pour {key}:\n")
    for context in contexts:
        print(context)

# Afficher un nombre limité de contextes pour chaque clé
'''LIMIT = 5  # Nombre de contextes à afficher par clé

for key, contexts in contexts_dict.items():
    print(f"\nContexte pour {key}:\n")
    for i, context in enumerate(contexts):
        if i < LIMIT:
            print(context)
        else:
            break
    print(f"... et {len(contexts) - LIMIT} contextes supplémentaires\n" if len(contexts) > LIMIT else "")'''

# Enregistrer le dictionnaire des contextes dans un fichier
with open('./contexts_dict.pkl', 'wb') as file:
    pickle.dump(contexts_dict, file)