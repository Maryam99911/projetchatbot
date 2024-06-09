from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Sélectionner la base de données
db = client['ProjetChatbot']

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




