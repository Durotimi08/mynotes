# mynotes/utils.py

import json

def load_json_data():
    try:
        with open("temporaryDb.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"session": "", "groups": []}

def update_json_data(data):
    with open("temporaryDb.json", "w") as f:
        json.dump(data, f)

def get_current_user_id():
    return load_json_data()["session"]

def create_group_if_not_exists(group_name):
    data = load_json_data()

    if all(i[0] != group_name for i in data["groups"]):
        data["groups"].append([group_name])
        update_json_data(data)

    # If you decide to switch to using a database, you can uncomment the following code:
    # with connect_to_database() as conn:
    #     cursor = conn.cursor()
    #     cursor.execute("""
    #         INSERT OR IGNORE INTO groups (group_name, user_id)
    #         VALUES (?, ?)
    #     """, (group_name, user_id))
    #     conn.commit()
