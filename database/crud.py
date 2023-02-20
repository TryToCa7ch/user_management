from sqlalchemy.orm import Session

from . import models, schemas

from utils import Mikrotik_helper


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, full_name = user.full_name, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_mikrotik_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Mikrotik_user).offset(skip).limit(limit).all()


def create_mikrotik_user(db: Session, item: schemas.MikrotikUserCreate, user_id: int):
    db_item = models.Mikrotik_user(username=item.username, password=item.password, user_id=item.user_id)
    db.add(db_item)  
    mh = Mikrotik_helper()
    mh.add_secret(username=item.username, password=item.password)
    db.commit()
    db.refresh(db_item)  
    return db_item