from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Sélectionner la base de données
db = client['ProjetChatbot']

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
