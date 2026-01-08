from app.security.encryption import Encryptor
from app.config.settings import settings

class APIKeyManager:
    def __init__(self):
        self.encryptor = Encryptor(settings.ENCRYPTION_KEY)
        self._store = {}

    def save_keys(self, user_id, api_key, secret):
        self._store[user_id] = {
            "api_key": self.encryptor.encrypt(api_key),
            "secret": self.encryptor.encrypt(secret)
        }

    def load_keys(self, user_id):
        data = self._store.get(user_id)
        if not data:
            raise ValueError("API keys not found")
        return {
            "api_key": self.encryptor.decrypt(data["api_key"]),
            "secret": self.encryptor.decrypt(data["secret"])
        }
