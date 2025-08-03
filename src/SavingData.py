from cryptography.fernet import Fernet
import json
import os

class SavingData:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_password(self):
        # Get the main project directory (one level up from src)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_dir = os.path.dirname(current_dir)
        
        # Define file paths in the main project directory
        key_file_path = os.path.join(project_dir, "secret.key")
        json_file_path = os.path.join(project_dir, "passwords.json")
        
        # Generate or load key (you might want to save this key securely)
        try:
            with open(key_file_path, "rb") as key_file:
                key = key_file.read()
        except FileNotFoundError:
            key = Fernet.generate_key()
            with open(key_file_path, "wb") as key_file:
                key_file.write(key)
        
        # Create Fernet instance
        fernet = Fernet(key)
        
        # Encrypt the data
        encrypted_password = fernet.encrypt(self.password.encode())
        encrypted_username = fernet.encrypt(self.username.encode())
        
        # Load existing data or create new structure
        try:
            with open(json_file_path, "r") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {"passwords": []}
        
        # Add new password entry
        new_entry = {
            "username": encrypted_username.decode(),
            "password": encrypted_password.decode()
        }
        data["passwords"].append(new_entry)
        
        # Save updated data
        with open(json_file_path, "w") as f:
            json.dump(data, f, indent=2)

