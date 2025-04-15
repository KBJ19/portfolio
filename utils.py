import json
import random

def load_data():
    with open("data.json", "r") as f:
        return json.load(f)

def generate_response(query, data):
    query = query.lower()
    if "project" in query:
        return "Khushal has worked on: " + ", ".join(data["projects"][:3])
    elif "skill" in query:
        return "Here are some of Khushal's top skills: " + ", ".join(data["skills"])
    elif "achievement" in query:
        return random.choice(data["achievements"])
    elif "contact" in query:
        return "You can reach Khushal at: " + data["contact"]
    else:
        return "Hmm, I didn't get that. Try asking about projects, skills, or achievements."
