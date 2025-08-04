from cryptography.fernet import Fernet
import json
import os

class SavingData: #This class is used to save the password and username to the json file
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
        
        # Generate or load key
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
            
class accessingData: #this class is used to access the password from the json file
    def __init__(self, username):
        self.username = username
    
    def access_password(self):
        # Get the main project directory (one level up from src)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_dir = os.path.dirname(current_dir)
        
        # Define file paths in the main project directory
        key_file_path = os.path.join(project_dir, "secret.key")
        json_file_path = os.path.join(project_dir, "passwords.json")
        
        # Load the encryption key
        try:
            with open(key_file_path, "rb") as key_file:
                key = key_file.read()
        except FileNotFoundError:
            return "No encryption key found"
        
        # Create Fernet instance
        fernet = Fernet(key)
        
        # Load the passwords data
        try:
            with open(json_file_path, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            return "No passwords file found"
        
        # Find and decrypt the password
        for entry in data["passwords"]:
            try:
                # Decrypt the username to compare
                decrypted_username = fernet.decrypt(entry["username"].encode()).decode()
                if decrypted_username == self.username:
                    # Decrypt and return the password
                    decrypted_password = fernet.decrypt(entry["password"].encode()).decode()
                    return f"Password for {self.username}: {decrypted_password}"
            except Exception as e:
                continue
        
        return f"No password found for username: {self.username}"

