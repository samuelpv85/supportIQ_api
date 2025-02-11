from sqlalchemy.orm import Session
from app.models.models import User
# from app.models.user_model import User
from app.schemas import UserCreate

def create_user(db: Session, user: UserCreate):
    new_user = User(username=user.username, password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()



# create_user() → Inserta un nuevo usuario en la BD.
# get_user() → Busca un usuario por ID.