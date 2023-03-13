from pydantic import BaseModel
from typing import Optional

class MikrotikUserBase(BaseModel):
    username: str
    user_id: int

class MikrotikUserCreate(MikrotikUserBase):
    password: str

class MikrotikUser(MikrotikUserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

class PortainerUserBase(BaseModel):
    username: str
    role: int
    user_id: int

class PortainerUserCreate(PortainerUserBase):
    password: str

class PortainerUser(PortainerUserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

class PortainerUserUpdate(PortainerUserBase):
    id: int

class UserBase(BaseModel):
    full_name: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    mikrotik_user: Optional[MikrotikUser]
    portainer_user: Optional[PortainerUser]

    class Config:
        orm_mode = True