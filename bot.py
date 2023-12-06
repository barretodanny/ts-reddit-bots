from api import create_session
import json

# takes in login credentials and returns tokens or -1 is log in failed
def login(email, password):
    login_payload = {"email": email, "password": password}
    req = create_session(login_payload)

    # failed to log in
    if (req.status_code != 201):
        print("Failed to log in bot. Exiting.")
        exit()
    
    data = json.loads(req.text)
    return data

