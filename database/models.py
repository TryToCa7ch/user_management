from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Mikrotik_user(Base):
    __tablename__ = 'mikrotik_user'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    user_id = Column(Integer, ForeignKey("users.id")) 

    main_user = relationship("User", back_populates="mikrotik_user", uselist=False)

class Portainer_user(Base):
    __tablename__ = 'portainer_user'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(Integer)
    is_active = Column(Boolean, default=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    main_user = relationship("User", back_populates="portainer_user", uselist=False)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    mikrotik_user = relationship("Mikrotik_user", back_populates="main_user", uselist=False)
    
    portainer_user = relationship("Portainer_user", back_populates="main_user", uselist=False)