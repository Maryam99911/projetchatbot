import spacy
import numpy as np
from transformers import pipeline
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from Loadaidesfinanicerescvec import contexts_aides_financieres
from Loadassociationetudiantes import contexts_associations_etudiantes
from LoadChiffresClésSuruniversitéevry import contexts_chiffres_cles_universite
from LoadBatimentsetServicesUniversiteEvry import contexts_batiments_services
from LoadCaractéristiquesDesEtudiants import contexts_caracteristiques_etudiants
from LoadTauxDeRéussite import contexts_taux_reussite

# Charger le modèle SpaCy avec Word2Vec embeddings
nlp = spacy.load('en_core_web_md')

# Charger le pipeline pour la question-réponse
#qa_pipeline = pipeline('question-answering', model='distilbert-base-cased-distilled-squad')

#qa_pipeline = pipeline("question-answering", model="TARUNBHATT/flan-t5-small-finetuned-squad")

qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")


# Préparer les contextes (simulés pour ce test)

contexts_dict = {
    "aides_financieres": contexts_aides_financieres,
    "associations_etudiantes": contexts_associations_etudiantes,
    "ChiffresClésSurL'universitéD'evry":contexts_chiffres_cles_universite,
    "BâtimentsetServicesdel'Universitéd'Evry":contexts_batiments_services,
    "CaractéristiquesDesEtudiants":contexts_caracteristiques_etudiants,
    "TauxDeRéussite":contexts_taux_reussite
}


# Fonction pour trouver le fichier JSON pertinent en utilisant les embeddings de mot
def find_relevant_file(question, contexts_dict, embeddings_model):
    relevant_file = None
    max_similarity = -1

    question_embedding = embeddings_model.encode(question)

    for file_name, contexts in contexts_dict.items():
        for context in contexts:
            context_embedding = embeddings_model.encode(context)
            similarity = np.dot(question_embedding, context_embedding) / (np.linalg.norm(question_embedding) * np.linalg.norm(context_embedding))
            if similarity > max_similarity:
                max_similarity = similarity
                relevant_file = file_name

    return relevant_file



# Charger le modèle d'embedddding de  RoBERTa
#roberta_model_name = 'sentence-transformers/roberta-large-nli-stsb-mean-tokens'


# Charger le modèle SentenceTransformer
model_name = "all-MiniLM-L6-v2"
embeddings_model = SentenceTransformer(model_name)





# Fonction pour trouver le contexte pertinent en utilisant les embeddings de mot
def find_similar_passages(question, contexts, threshold=0.6):
    # Obtenir les embeddings de la question
    question_embedding = embeddings_model.encode(question)

    # Initialiser la liste des passages similaires
    similar_passages = []

    #print(contexts)

    # Parcourir chaque contexte
    for context in contexts:
        # Obtenir l'embedding du contexte
        context_embedding = embeddings_model.encode(context)

        # Calculer la similarité entre la question et le contexte
        similarity = cosine_similarity(question_embedding.reshape(1, -1), context_embedding.reshape(1, -1))[0][0]

        # Vérifier si la similarité est supérieure au seuil
        if similarity >= threshold:
            # Ajouter le contexte à la liste des passages similaires
            similar_passages.append((context, similarity))

    return similar_passages

def find_one_similar_passages(question, contexts):
    # Obtenir les embeddings de la question
    max_similarity = -1
    question_embedding = embeddings_model.encode(question)

    #print(contexts)

    # Parcourir chaque contexte
    for context in contexts:
        # Obtenir l'embedding du contexte
        context_embedding = embeddings_model.encode(context)

        # Calculer la similarité entre la question et le contexte
        new_similarity = cosine_similarity(question_embedding.reshape(1, -1), context_embedding.reshape(1, -1))[0][0]


        if new_similarity >= max_similarity:
         # Ajouter le contexte à la liste des passages similaires
            relevant_context = context
            max_similarity = new_similarity

    return relevant_context,max_similarity




# Fonction pour extraire des informations
def extract_information(question, passages):
    answers = []
    context = " ".join(passages)
    #print(context)
    result  = qa_pipeline({"context": context, "question": question})
    for passage in passages:
        result = qa_pipeline({"context": passage, "question": question})
        answers.append(result['answer'])


    return result['answer']

# Fonction pour agréger les résultats
def aggregate_results(question, answers):
    if "Somme" in question.lower():
        unique_answers = set(answers)
        return len(unique_answers)
    elif "calcule" in question.lower():
        total = sum(int(answer) for answer in answers if answer.isdigit())
        return total
    else:
        return answers


# Fonction pour obtenir la réponse en utilisant une approche combinée
def get_answer_combined(question, contexts_dict):
    relevant_file = None
    max_similarity = -1
    # Liste de salutations courantes
    greetings = ["bonjour", "salut", "hello", "hi"]

    # Réponses aux salutations
    greeting_responses = ["Bonjour! Comment puis-je vous aider aujourd'hui?",
                          "Salut! Que puis-je faire pour vous?",
                          "Hello! En quoi puis-je vous être utile?"]

    # Normaliser l'entrée de l'utilisateur
    question_lower = question.lower()

    # Vérifier si l'entrée de l'utilisateur est une salutation
    for greeting in greetings:
        if greeting in question_lower:
            return np.random.choice(greeting_responses)

    # Trouver le fichier pertinent
    relevant_file = find_relevant_file(question, contexts_dict, embeddings_model)

    threshold = 0
    print(relevant_file)
    if relevant_file:
        # Trouver les passages similaires
        similar_passages = find_similar_passages(question, contexts_dict[relevant_file])
        print(similar_passages)

        # Extraire les informations pertinentes
        answers = extract_information(question, similar_passages)

        # Agréger les résultats pour répondre à la question
        final_answer = aggregate_results(question, answers)
        return final_answer



#qui est le president de l'association A ?
print('Bonjour je suis le chatbot IA de Paris Saclay')


# Test cases
test_questions = [
    "Combien de dossiers ont été déposés en 2019 ?",
    "Quel est le président de l'association A ?",
    "Parle moi de l'association esthesie?",
    "Où se localise le batiment DVEC et le bâtiment IUT Bretigny?"
]

# Expected results
expected_results = [
    "500",
    "Jean Dupont",
    "Reunir differents artistes autour de projets ",
    "le sport"
]

# Testing the function
for question, expected in zip(test_questions, expected_results):
    answer = get_answer_combined(question, contexts_dict)
    print(f"Question: {question}")
    print(f"Expected: {expected}, Got: {answer}")
    print("Test Passed!" if answer == expected else "Test Failed!")
    print()
#parle moi de l'association esthesie ?

# while True:
#     question = input("Question: ")
#     answer = get_answer_combined(question, contexts_dict)
#     print(answer)
