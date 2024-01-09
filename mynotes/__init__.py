# mynotes/__init__.py

import sys
from .db import syncData
from .commands import add_note_to_group, list_notes, delete_note, register_user, login_user, jsonData
from .utils import get_current_user_id

def main():
    if len(sys.argv) < 2:
        print("Usage: notes -<group_name> <note_text>")
        sys.exit(1)

    command = sys.argv[1][1:]

    if command == "delete":
        if len(sys.argv) < 3:
            print("Usage: notes -delete <unique_id>")
            sys.exit(1)

        unique_id = sys.argv[2]
        delete_note(unique_id)

    elif command == "register":
        if len(sys.argv) != 4:
            print("Usage: notes -register <username> <password>")
            sys.exit(1)

        username = sys.argv[2]
        password = sys.argv[3]
        register_user(username, password)

    elif command == "login":
        if len(sys.argv) != 4:
            print("Usage: notes -login <username> <password>")
            sys.exit(1)

        username = sys.argv[2]
        password = sys.argv[3]
        user_id = login_user(username, password)

        if user_id:
            print("Successfully logged in")

    elif command == "ls":
        if len(sys.argv) != 3:
            print("Usage: notes -ls <group_name>")
            sys.exit(1)
        else:
            group_name = sys.argv[2]
            list_notes(group_name)

    elif command == "push":
        if jsonData()["session"] == "":
            print("Please login or register to push notes")
        else:
            try:
                syncData()
            except:
                print("An error occured when connection to your account")
            finally:
                print("Succesfully synced with your account")
    else:
        group_name = command
        note_text = " ".join(sys.argv[2:])
        add_note_to_group(note_text, group_name)


if __name__ == "__main__":
    main()
