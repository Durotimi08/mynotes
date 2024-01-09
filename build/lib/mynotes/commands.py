# mynotes/commands.py

import uuid,json
from datetime import datetime
from .db import create_user, authenticate_user

def jsonData():
    try:
        with open("temporaryDb.json", "r") as f:
            x = json.load(f)
        return x
    except FileNotFoundError:
        return {"notes": []}

def updateJsonData(notes):
    with open("temporaryDb.json", "w") as f:
        json.dump({"notes": notes}, f)

def register_user(username, password):
    create_user(username, password)
    user_id = authenticate_user(username, password)
    print(f"User '{username}' registered successfully.")

def login_user(username, password):
    user_id = authenticate_user(username, password)
    if user_id:
        print(f"User '{username}' logged in successfully. User ID: {user_id}")
        return user_id
    else:
        print("Invalid username or password.")
        return None

def add_note_to_group(note_text, group_name):
    unique_id = generate_unique_id()

    timestamp = datetime.timestamp(datetime.now())

    note = [unique_id, timestamp, note_text, group_name]
    data = jsonData()
    data["notes"].append(note)
    updateJsonData(data["notes"])

    print(f"Note added to '{group_name}' successfully. ID: {unique_id}")

def list_notes(group_name):
    notes = jsonData()["notes"]
    notes = [note for note in notes if note[3] == group_name]

    for note in notes:
        dt_object = datetime.fromtimestamp(note[1])
        formatted_date_time = dt_object.strftime("%Y-%m-%d %H:%M:%S")
        print(f"{note[0]} \n {note[2]} ({note[3]} @ {formatted_date_time})")

def delete_note(unique_id):
    notes = jsonData()["notes"]
    notes = [note for note in notes if note[0] != unique_id]
    updateJsonData(notes)

def generate_unique_id():
    return str(uuid.uuid4())
