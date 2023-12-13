from api import *
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

def send_post(title, content, subreddit_name, token):
    req = get_subreddit_by_name(subreddit_name)

    # subreddit not found
    if (req.status_code != 200):
        print(f"Error fetching {subreddit_name}. Exiting.")
        exit()
    
    subreddit = json.loads(req.text)
    subreddit_id = subreddit["_id"]

    post_payload = {"title": title, "content": content, "subreddit": subreddit_id}
    req = create_post(post_payload, token)

    # failed to create post
    if (req.status_code != 201):
        print("Failed to create post.")
        return
    