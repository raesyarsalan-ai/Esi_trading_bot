from app.users.user_model import User
from app.config.settings import settings

class SessionManager:
    def create_user(self, user_id):
        is_admin = user_id == settings.ADMIN_USER_ID
        return User(
            user_id=user_id,
            is_admin=is_admin,
            is_active=is_admin
        )
