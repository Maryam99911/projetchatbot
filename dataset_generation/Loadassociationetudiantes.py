from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Sélectionner la base de données
db = client['ProjetChatbot']

# Sélectionner la collection
collection = db['associations-etudiantes']

# Récupérer les documents de la collection
documents= collection.find()
documents2= collection.find()


# Fonction pour construire les contextes
def construire_contextes_associations_questions(data):
    contexts = []
    for entry in data:
        # Gestion des valeurs None ou manquantes
        code_postal = int(entry['code_postal']) if entry.get('code_postal') is not None else 'inconnu'
        numero_de_voie = int(entry['numero_de_voie']) if entry.get('numero_de_voie') is not None else 'inconnu'
        voie = entry.get('voie', 'voie inconnue')
        adresse = f"{numero_de_voie}  {voie} {code_postal} "
        reseaux_sociaux = entry.get('reseaux_sociaux', 'pas de réseaux sociaux').lower() if entry.get('reseaux_sociaux') else 'pas de réseaux sociaux'
        president = entry['president']
        description = entry['description']


        context_adresse = (f"l'{entry['nom'].lower()}  a pour Adresse : {adresse.lower()}")
        contexts.append(context_adresse)
        context_president = (f"l'{entry['nom'].lower()} " f" a pour President  :  <hl>{president.lower()}<hl>")
        contexts.append(context_president)
        context_rs = (f"l' {entry['nom'].lower()} "f" a pour Reseaux sociaux : <hl>{reseaux_sociaux.lower()}<hl>")
        contexts.append(context_rs)
        context_objectif = (f"l'{entry['nom'].lower()} "f"a pour Objectif {description.lower()}." )
        contexts.append(context_objectif)
    return contexts


def construire_contextes_associations_reponses(data):
    contexts_reponses = []

    for entry in data:
        # Gestion des valeurs None ou manquantes
        code_postal = int(entry['code_postal']) if entry.get('code_postal') is not None else 'inconnu'
        numero_de_voie = int(entry['numero_de_voie']) if entry.get('numero_de_voie') is not None else 'inconnu'
        voie = entry.get('voie', 'voie inconnue')
        adresse = f"{numero_de_voie}  {voie} {code_postal} "
        reseaux_sociaux = entry.get('reseaux_sociaux', 'pas de réseaux sociaux').lower() if entry.get('reseaux_sociaux') else 'pas de réseaux sociaux'
        president = entry['president']
        description = entry['description']

        context = (f"l'{entry['nom'].lower()}  a pour adresse  {adresse}")
        contexts_reponses.append(context)
        context = (f"l'{entry['nom'].lower()} " f" a pour president    {president}")
        contexts_reponses.append(context)
        context = (f"l' {entry['nom'].lower()} "f" a pour reseaux sociaux  {reseaux_sociaux}")
        contexts_reponses.append(context)
        context = (f"l'{entry['nom'].lower()} "f"a pour objectif {description}." )
        contexts_reponses.append(context)
    return contexts_reponses

# Construire les contextes à partir des documents récupérés
contexts_associations_etudiantes_questions = construire_contextes_associations_questions(documents)
contexts_associations_etudiantes_reponses = construire_contextes_associations_reponses(documents2)

