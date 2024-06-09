from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Sélectionner la base de données
db = client['ProjetChatbot']

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
