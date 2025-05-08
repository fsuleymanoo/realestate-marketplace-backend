from app.models.profile import Profile
from app.extensions import db
from typing import Optional
from sqlalchemy import select

class ProfileRepository:
    @staticmethod
    def create(user_id:int, **kwargs) -> Profile:
        profile = Profile(user_id=user_id)

        for key, value in kwargs.items():
            if hasattr(profile, key):
                setattr(profile, key, value)

        db.session.add(profile)
        db.session.commit()
        return profile        
    
    @staticmethod
    def get_by_id(profile_id: int) -> Optional[Profile]:
        stmt = select(Profile).where(Profile.id == profile_id)
        result = db.session.execute(stmt)
        return result.scalars().first()
    
    @staticmethod
    def get_by_user_id(user_id: int) -> Optional[Profile]:
        stmt = select(Profile).where(Profile.user_id == user_id)
        result = db.session.execute(stmt)
        return result.scalars().first()
    

    @staticmethod
    def update(profile: Profile) -> Profile:
        db.session.commit()
        return profile
    

    @staticmethod
    def delete(profile: Profile) -> bool:
        profile.is_deleted = True
        db.session.commit()
        return True
