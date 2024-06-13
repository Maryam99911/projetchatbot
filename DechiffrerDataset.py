from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from pymongo import MongoClient
import json


# Connecter à MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['ProjetChatbotEncryption']
collection = db['dataset_chiffré']

# Récupérer les données chiffrées depuis MongoDB
stored_data = collection.find_one()
#print(os.getcwd())
# Fonction pour charger la clé privée à partir d'un fichier
def get_private_key():
    with open("C:/Users/Khady/PycharmProjects/chatbotAI/GenerationDatasets/private_key.pem", "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )
    return private_key

# Fonction pour déchiffrer les données
def decrypt(encrypted_data, encrypted_key, iv):
    private_key = get_private_key()
    aes_key = private_key.decrypt(
        encrypted_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    cipher = Cipher(algorithms.AES(aes_key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

    return decrypted_data

# Déchiffrer les données
encrypted_key = stored_data['encrypted_key']
iv = stored_data['iv']
encrypted_data = stored_data['encrypted_data']
decrypted_data = decrypt(encrypted_data, encrypted_key, iv)
print("Données déchiffrées:", decrypted_data.decode('utf-8'))

# Charger les données déchiffrées dans un objet JSON
json_data = json.loads(decrypted_data.decode('utf-8'))

# Convertir json_data en une chaîne JSON
json_string = json.dumps(json_data, indent=4)

# Écrire la chaîne JSON dans un fichier .json
with open("fichierfinal.json", "w") as json_file:
    json_file.write(json_string)

# Utiliser le fichier .json dans votre code
with open("fichierfinal.json", encoding='utf-8') as file:
    data = json.load(file)