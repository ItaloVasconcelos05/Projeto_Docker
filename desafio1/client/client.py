import time
import requests

SERVER_URL = "http://servidor:8080"

while True:
    try:
        response = requests.get(SERVER_URL)
        print("Respodsta do servidor:", response.text, flush= True)
        
    except Exception as e:
        print("Erro ao conectar:", e, flush= True)
    time.sleep(5)
    
    