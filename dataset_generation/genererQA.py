from transformers import pipeline
import json
from Loadassociationetudiantes import contexts_associations_etudiantes_questions,contexts_associations_etudiantes_reponses
from Loadaidesfinanicerescvec import contextes_aides_financieres_questions, contextes_aides_financieres_reponses
from LoadBatimentsetServicesUniversiteEvry import contextes_batiments_services_questions, contextes_batiments_services_reponses
from LoadChiffresClésSuruniversitéevry import contexts_chiffres_cles_universite_questions, contexts_chiffres_cles_universite_reponses
from LoadCaractéristiquesDesEtudiants import contexts_caracteristiques_etudiants_questions_2023, contexts_caracteristiques_etudiants_reponses_2023
from LoadTauxDeRéussite import contexts_taux_reussite_questions, contexts_taux_reussite_questions

pipe_question = pipeline("text2text-generation", model="lincoln/barthez-squadFR-fquad-piaf-question-generation")
qa_pipeline = pipeline("question-answering", model="TARUNBHATT/flan-t5-small-finetuned-squad")


# Construire la liste de tuples (context_question, context_reponse)
contexts_associations_etudiantes = zip(contexts_associations_etudiantes_questions, contexts_associations_etudiantes_reponses)
contextes_aides_financieres = zip(contextes_aides_financieres_questions, contextes_aides_financieres_reponses)
contextes_batiments_services = zip(contextes_batiments_services_questions, contextes_batiments_services_reponses)
contexts_taux_reussite = zip(contexts_taux_reussite_questions,contexts_taux_reussite_questions)
contexts_chiffres_cles_universite = zip(contexts_chiffres_cles_universite_questions,contexts_chiffres_cles_universite_reponses)
contexts_caracteristiques_etudiants = zip(contexts_caracteristiques_etudiants_questions_2023,contexts_caracteristiques_etudiants_reponses_2023)




def remplir_dataset_adresses_services(context_ensemble):
    tag_unite_ensemble = []
    cpt=0
    for context_question, context_reponse in context_ensemble:
        cpt = cpt+1

        question = f" Quelle est l'adresse de  {context_question}"
        print('question : ', question)

        answer = f"L'adresse de {context_question} est : {context_reponse}"
        print('answer : ', answer)

        tag_unite = {"tag": str(cpt),
         "patterns": [question],
         "responses": [answer]
         }
        tag_unite_ensemble.append(tag_unite)

    return tag_unite_ensemble

def remplir_dataset_adresses_taux_de_reussite(context_ensemble):
    cpt=0
    tag_unite_ensemble = []
    for context_question, context_reponse in context_ensemble:
        print('question : ', context_question)
        print('answer : ', context_reponse)
        tag_unite = {"tag": str(cpt),
         "patterns": [context_question],
         "responses": [context_reponse]
         }
        tag_unite_ensemble.append(tag_unite)

    return tag_unite_ensemble

def remplir_dataset_caracteristiques_etudiants(context_ensemble):
    cpt=0
    tag_unite_ensemble = []
    for context_question, context_reponse in context_ensemble:
        print('question : ', context_question)
        print('answer : ', context_reponse)
        tag_unite = {"tag": str(cpt),
         "patterns": [context_question],
         "responses": [context_reponse]
         }
        tag_unite_ensemble.append(tag_unite)

    return tag_unite_ensemble
def remplir_dataset(context_ensemble):
    cpt=0
    tag_unite_ensemble = []
    for context_question, context_reponse in context_ensemble:
        cpt = cpt+1
        print('context_reponse : ', context_reponse)

        # Générer la question à partir du contexte
        generated_question = pipe_question(context_question)

        # Extraire la question générée (en tant que chaîne de caractères)
        question = generated_question[0]['generated_text']
        print('question : ', question)

        # Utiliser la pipeline de question-réponse pour obtenir la réponse
        answer = qa_pipeline(question=question, context=context_reponse)

        # Vérifier si la réponse est une chaîne vide
        if not answer['answer']:
            # Remplacer la réponse par context_reponses
            answer['answer'] = context_reponse

        print('answer : ', answer['answer'])

        tag_unite = {"tag": str(cpt),
         "patterns": [question],
         "responses": [answer['answer']]
         }
        tag_unite_ensemble.append(tag_unite)

    return tag_unite_ensemble


def generer_dataset_final():
    with open('data.json', 'r') as f:
        data = json.load(f)

    # S'assurer que la clé "intents" existe dans le dictionnaire
    if "intents" not in data:
        data["intents"] = []

    # Compteur pour les tags dynamiques
    cpt = len(data["intents"]) + 1

    # Appeler les fonctions pour remplir les différents tags dynamiques
    datasets = [
        remplir_dataset(contextes_aides_financieres),
        remplir_dataset_adresses_services(contextes_batiments_services),
        remplir_dataset_adresses_taux_de_reussite(contexts_taux_reussite),
        remplir_dataset(contexts_chiffres_cles_universite),
        remplir_dataset_caracteristiques_etudiants(contexts_caracteristiques_etudiants),
        remplir_dataset(contexts_associations_etudiantes)
    ]

    # Ajouter les tags dynamiques au dictionnaire 'intents'
    for dataset in datasets:
        for tag_unite in dataset:
            data["intents"].append({
                "tag": f"tag_unite_{cpt}",
                "patterns": tag_unite["patterns"],
                "responses": tag_unite["responses"]
            })
            cpt += 1


    combine_data = json.dumps(data, indent=4)


    return combine_data



combine_data = generer_dataset_final()







