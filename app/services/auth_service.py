from app.repositories.user_repository import UserRepository
from app.models.user import User
from typing import Optional
from app.repositories.profile_repository import ProfileRepository

class AuthService:
    @staticmethod
    def register(email: str, username: str, password:str) -> User:
        if UserRepository.get_by_email(email):
            raise ValueError(f"Email '{email} already exists")
        
        if UserRepository.get_by_email(username):
            raise ValueError(f"Username '{username} already exists")
        
        user = UserRepository.create_user(email, username, password)

        ProfileRepository.create(user.id)

        return user