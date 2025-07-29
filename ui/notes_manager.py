import os
import json
from cryptography.fernet import Fernet

KEY_FILE = "notes.key"
NOTES_FILE = "notes.json.enc"

def get_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)
    else:
        with open(KEY_FILE, "rb") as f:
            key = f.read()
    return key

fernet = Fernet(get_key())

def save_notes(notes):
    data = [{"title": note["title"], "content": note["content"], "files": note.get("files", [])} for note in notes]
    json_data = json.dumps(data).encode()
    encrypted = fernet.encrypt(json_data)
    with open(NOTES_FILE, "wb") as f:
        f.write(encrypted)

def load_notes():
    if not os.path.exists(NOTES_FILE):
        return []
    with open(NOTES_FILE, "rb") as f:
        encrypted = f.read()
    try:
        decrypted = fernet.decrypt(encrypted)
        data = json.loads(decrypted.decode())
        return data
    except Exception:
        return []