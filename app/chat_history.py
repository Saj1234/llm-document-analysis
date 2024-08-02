import os
import os.path
import json

def load_chat_history(session_id):
    """Function loading saved chat history."""
    # Check if file exist with session id. if not, this is a new conversation
    file_path = "./temp/" + session_id + ".json"
    if os.path.isfile(file_path):
        file = open(file_path, encoding="utf-8")
        data = json.load(file)
        if "chat_history" in data:
            return data["chat_history"]

    return []

def save_chat_history(session_id, chat_history):
    """Function saving chat history."""
    file_path = "./temp/" + session_id + ".json"
    data = {"chat_history": chat_history}

    json_data = json.dumps(data, indent=4)
    with open(file_path, "w", encoding="utf-8") as outfile:
        outfile.write(json_data)

def clear_chat_history():
    """Function clearing temp chat history files."""
    try:
        directory_path = "./temp"
        files = os.listdir(directory_path)

        for file in files:
            file_path = os.path.join(directory_path, file)

            if os.path.isfile(file_path):
                os.remove(file_path)

        return "All temp files deleted successfully."

    except OSError:
        return "Error occurred while deleting files."
