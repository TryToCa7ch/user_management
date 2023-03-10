from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from database import crud, models, schemas
from database.database import SessionLocal, engine

from pydantic.error_wrappers import ValidationError

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def main_page():
    return "Main page"

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/mikrotik_user/", response_model=schemas.MikrotikUser)
def create_mikrotik_user_for_user(
    user_id: int, item: schemas.MikrotikUserCreate, db: Session = Depends(get_db)
):
    return crud.create_mikrotik_user(db=db, item=item, user_id=user_id)


@app.get("/mikrotik_users/", response_model=list[schemas.MikrotikUser])
def get_mikrotik_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_mikrotik_users(db, skip=skip, limit=limit)
    return items

@app.get("/portainer_users/", response_model=list[schemas.PortainerUser])
def get_portainer_user(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_portainer_users(db, skip=skip, limit=limit)

@app.post("/users/{user_id}/portainer_user/", response_model=schemas.PortainerUser)
def create_portainer_user_for_user(
    user_id: int, item: schemas.PortainerUserCreate, db: Session = Depends(get_db)
):
    try:
        db_item = crud.create_portainer_user(db=db, item=item)
        return db_item
    except:
        raise HTTPException(status_code=400, detail='Password does not meet the requirements')