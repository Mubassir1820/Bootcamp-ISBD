from sqlalchemy import func
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import Optional
from db.models.user import User
from fastapi import Depends, HTTPException
from utils.jwt_manager import verify_token
from utils.password_manager import PasswordManager
from fastapi.security import OAuth2PasswordBearer
from db.session import get_db
from utils.password_manager import PasswordManager
from fastapi import status

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=" /users/token")


class UserRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def get_user_by_email(self, email: str) -> Optional[User]:
       return self.db.query(User).filter(func.lower(User.email) == func.lower(email)).first()

    def create_user(self, email: str, password: str) -> User:
        _hashed_password = PasswordManager.get_password_hash(password=password)
        db_user = User(email=email, password=_hashed_password)
        self.db.add(db_user)
        try:
            self.db.commit()
            self.db.refresh(db_user)
        except IntegrityError:
            self.db.rollback()
            raise HTTPException(status_code=400, detail="Email already registered")
        return db_user
    
    def get_user_by_id(self, id: int) -> Optional[User]:
       return self.db.query(User).filter(User.id == id).first()
    
    def get_user_for_token(self, email: str, password: str) -> Optional[User]:
       user = self.get_user_by_email(email=email)
       if not user:
           raise HTTPException(status_code=401, detail="Invalid credentials")
       is_password_matched = PasswordManager.verify_password(password, user.password)
       if not is_password_matched:
           raise HTTPException(status_code=401, detail="Invalid credentials")
       return user
    
    @staticmethod
    def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
       payload = verify_token(token)
       
       if payload is None:
           raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
       user = db.query(User).filter(User.id == payload.get("sub")).first()
       if user is None:
           raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
       return user
