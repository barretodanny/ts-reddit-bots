import requests
import json

LOGIN_ENDPOINT = "https://ts-reddit-rest-api.onrender.com/api/sessions"

# takes in login credentials and returns tokens or -1 is log in failed
def login(email, password):
    login_payload = {"email": email, "password": password}
    req = requests.post(LOGIN_ENDPOINT, json=login_payload)

    # failed to log in
    if (req.status_code != 201):
        return -1
    
    data = json.loads(req.text)
    return data