from http.client import responses

import requests
url = "http://localhost:11434/api/generate"

payload = {"model":"llama3.2:3b"
    ,"prompt":"How many people live in TLV?, give my a short answer!"
    ,"stream":False}
responses = requests.post(url, json=payload)
print(responses.json()["response"])

