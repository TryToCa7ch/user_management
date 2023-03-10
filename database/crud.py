from sqlalchemy.orm import Session

from . import models, schemas

from utils import MikrotikHelper
from utils import PortainerHelper


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
    fake_hashed_password = item.password + "notreallyhashed"
    db_item = models.Mikrotik_user(username=item.username, hashed_password=fake_hashed_password, user_id=item.user_id)
    db.add(db_item)  
    mh = MikrotikHelper()
    mh.add_secret(username=item.username, password=item.password)
    db.commit()
    db.refresh(db_item)  
    return db_item

def get_portainer_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Portainer_user).offset(skip).limit(limit).all()

def create_portainer_user(db: Session, item: schemas.PortainerUserCreate):
    fake_hashed_password = item.password + "notreallyhashed"
    db_item = models.Portainer_user(username=item.username, hashed_password=fake_hashed_password, user_id=item.user_id, role=item.role, is_active=True)
    db.add(db_item)
    ph = PortainerHelper()
    try:
        ph.add_user(username=item.username, password=item.password, role=item.role)
    except:
        raise Exception
    db.commit()
    db.refresh(db_item)
    return db_item