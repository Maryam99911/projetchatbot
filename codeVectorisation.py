import spacy
from transformers import pipeline
from sentence_transformers import SentenceTransformer, util
import numpy as np
import pickle

# Charger le dictionnaire des contextes à partir du fichier
with open('contexts_dict.pkl', 'rb') as file:
    contexts_dict = pickle.load(file)

#print(contexts_dict)

contexts = []

# Itérer sur les valeurs du dictionnaire et ajouter chaque élément à la liste
for value in contexts_dict.values():
    contexts.extend(value)

#print(contexts)

'''contexts = [
    "Le Mont Everest est le plus haut sommet du monde, culminant à 8 848 mètres.",
    "La pizza est un plat italien populaire composé d'une pâte garnie de sauce tomate, de fromage et divers autres ingrédients.",
    "Les girafes sont connues pour leur long cou, qui leur permet d'atteindre les feuilles des arbres les plus hauts.",
    "La gravité est la force qui attire les objets vers le centre de la Terre.",
    "Le système solaire comprend huit planètes qui orbitent autour du Soleil.",
    "entre 2019 et 2020, il y avait 600 dossiers déposés. En 2019, il y avait 170 dossiers déposés, 147 dossiers acceptés, avec un budget de 52693 euros et une aide moyenne de 358.455782313 euros. et En 2020, il y avait 430 dossiers déposés, 407 dossiers acceptés, avec un budget de 137656 euros et une aide moyenne de 338.221130221 euros. et En 2021, il y avait 92 dossiers déposés, 82 dossiers acceptés,avec un budget de 31301 euros et une aide moyenne de 381.719512195 euros."
]'''


# Charger le pipeline pour la question-réponse
#qa_pipeline = pipeline('question-answering', model='distilbert-base-cased-distilled-squad')
#qa_pipeline = pipeline("text2text-generation", model="google/flan-t5-small")
roberta_pipeline = pipeline('question-answering', model="deepset/roberta-base-squad2", tokenizer="deepset/roberta-base-squad2")
#qa_pipeline = pipeline("text-generation", model="google/gemma-1.1-7b-it")
#qa_pipeline = pipeline("question-answering", model="eren23/DistilHermes-2.5-Mistral-7B")


# Charger le modèle SpaCy avec Word2Vec embeddings
nlp = spacy.load('en_core_web_md')

def TrouverMeilleurContexte(question, contexts):
    model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
    question_embedding = model.encode(question)
    context_embeddings = model.encode(contexts)
    similarities = util.pytorch_cos_sim(question_embedding, context_embeddings).numpy()
    best_context_index = np.argmax(similarities)
    return contexts[best_context_index]

def main():
    print("Bienvenue à Chatbot Sacl'AI ! Posez-moi n'importe quelle question et je ferai de mon mieux pour y répondre. Pour quitter, tapez 'exit'.")
    while True:
        user_input = input("Posez une question (ou tapez 'exit' pour quitter) : ")
        if user_input.lower() == 'exit':
            break

        meilleur_contexte = TrouverMeilleurContexte(user_input, contexts)

        input_text = {
            'question': user_input,
            'context': meilleur_contexte
        }

        result = roberta_pipeline(input_text)

        response = {
            "input": input_text,
            "response": result if result else "Oups, je ne peux pas répondre à cette question pour l'instant. Essayez plus tard !",
            "context": meilleur_contexte
        }

        print(f"Input: {response['input']}")
        print(f"Response: {response['response']}")
        print(f"Context: {response['context']}\n")

if __name__ == '__main__':
    main()
