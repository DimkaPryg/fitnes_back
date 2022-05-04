from fastapi import APIRouter
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
from services import userinfo_service
from schemes import userinfo_scheme as scheme

app = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/userinfo/{userinfo_id}", response_model=scheme.UserInfo)
def get_userinfo(userinfo_id: int, db: Session = Depends(get_db)):
    db_userinfo = userinfo_service.get_by_id(db, userinfo_id=userinfo_id)
    if db_userinfo is None:
        raise HTTPException(status_code=404, detail="Userinfo not found")
    return db_userinfo


@app.get("/userinfo")
def get_all_userinfo(db: Session = Depends(get_db)):
    return userinfo_service.get_all(db)


@app.post("/userinfo", response_model=scheme.UserInfo)
def create_userinfo(userinfo: scheme.UserInfoBase, db: Session = Depends(get_db)):
    return userinfo_service.create(db=db, userinfo=userinfo)


@app.put("/userinfo/{userinfo_id}", response_model=scheme.UserInfo)
def update_userinfo(userinfo_id: int, userinfo: scheme.UserInfoBase, db: Session = Depends(get_db)):
    db_userinfo = userinfo_service.get_by_id(db, userinfo_id=userinfo_id)
    if db_userinfo is None:
        raise HTTPException(status_code=404, detail="Userinfo not found")
    return userinfo_service.update(db=db, userinfo_id=userinfo_id, userinfo=userinfo)


@app.put("/userinfo/{userinfo_id}", response_model=scheme.UserInfo)
def update_userinfo(userinfo_id: int, userinfo: scheme.UserInfoBase, db: Session = Depends(get_db)):
    db_userinfo = userinfo_service.get_by_id(db, userinfo_id=userinfo_id)
    if db_userinfo is None:
        raise HTTPException(status_code=404, detail="Userinfo not found")
    return userinfo_service.update(db=db, userinfo_id=userinfo_id, userinfo=userinfo)


@app.delete("/userinfo/{userinfo_id}", response_model=scheme.UserInfo)
def delete_article(userinfo_id: int, db: Session = Depends(get_db)):
    db_userinfo = userinfo_service.get_by_id(db, userinfo_id=userinfo_id)
    if db_userinfo is None:
        raise HTTPException(status_code=404, detail="Userinfo not found")
    return userinfo_service.delete(db=db, userinfo_id=userinfo_id)
