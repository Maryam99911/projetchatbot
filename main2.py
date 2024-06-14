
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.optimizers import Adam
from fastapi import FastAPI, HTTPException
from keras.src.optimizers import SGD
from pydantic import BaseModel
import numpy as np
import json
from fastapi.middleware.cors import CORSMiddleware
from nltk.stem import LancasterStemmer
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam
import pickle
import random
import nltk
import sys
import logging
import speech_recognition as sr

sys.stdout.reconfigure(encoding='utf-8')
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Autoriser que le chemin localhost:4200
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type", "Authorization"],
)


stemmer = LancasterStemmer()

# Load the intents file
with open("fichierfinal.json", encoding='utf-8') as file:
    data = json.load(file)

try:
    with open("data.pickle", "rb") as f:
        words, labels, training, output = pickle.load(f)
except:
    words = []
    labels = []
    docs_x = []
    docs_y = []

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            wrds = nltk.word_tokenize(pattern)
            words.extend(wrds)
            docs_x.append(wrds)
            docs_y.append(intent["tag"])

        if intent["tag"] not in labels:
            labels.append(intent["tag"])

    words = [stemmer.stem(w.lower()) for w in words if w != "?"]
    words = sorted(list(set(words)))

    labels = sorted(labels)

    training = []
    output = []

    out_empty = [0 for _ in range(len(labels))]

    for x, doc in enumerate(docs_x):
        bag = []

        wrds = [stemmer.stem(w.lower()) for w in doc]

        for w in words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)

        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1

        training.append(bag)
        output.append(output_row)

    training = np.array(training)
    output = np.array(output)

    with open("data.pickle", "wb") as f:
        pickle.dump((words, labels, training, output), f)

# Define the model
model = Sequential()
model.add(Dense(128, input_shape=(len(training[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(output[0]), activation='softmax'))

# Compile the model
#sgd = SGD(learning_rate=0.01, decay=1e-6, momentum=0.9, nesterov=True)
#model.compile(loss='categorical_crossent   ropy', optimizer=sgd, metrics=['accuracy'])
#model.compile(optimizer='adam',loss='mean_squared_error')
model.compile(optimizer=Adam(), loss='mean_squared_error', metrics=['accuracy'])
#model.compile(optimizer='adam', loss='mean_absolute_error', metrics=['mean_absolute_error'])

# Train the model
model.fit(training, output, epochs=2000, batch_size=5, verbose=1)
model.save("chatbot_model.h5")

# Function to convert user input into bag of words
def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]
    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]
    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
    return np.array(bag)


class QuestionRequest(BaseModel):
    question: str

def chat(question: str) -> str:
    try:
        results = model.predict(np.array([bag_of_words(question, words)]))[0]
        results_index = np.argmax(results)
        tag = labels[results_index]

        if results[results_index] > 0.7:
            for tg in data["intents"]:
                if tg['tag'] == tag:
                    responses = tg['responses']
            return random.choice(responses)
        else:
            return "Je n'ai pas compris, essayez encore une fois avec une touche de magie !"
    except Exception as e:
        logger.error(f"Error processing request: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/ask")
async def ask_question(request: QuestionRequest):
    question = request.question
    answer = chat(question)
    return {"answer": answer}



if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='127.0.0.1', port=8000)
