from sqlalchemy.orm import Session
from schemes import userinfo_scheme as scheme
import models


def get_by_id(db: Session, userinfo_id: int):
    return db.query(models.UserInfo).filter(models.UserInfo.id == userinfo_id).first()


def get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.UserInfo).offset(skip).limit(limit).all()


def create(db: Session, userinfo: scheme.UserInfoBase):
    db_userinfo = models.UserInfo(login=userinfo.login)
    db.add(db_userinfo)
    db.commit()
    db.refresh(db_userinfo)
    return db_userinfo


def update(db: Session, userinfo_id: int, userinfo: scheme.UserInfoBase):
    db_userinfo = get_by_id(db, userinfo_id)
    db_userinfo.login = userinfo.login
    db.commit()
    db.refresh(db_userinfo)
    return db_userinfo


def delete(db: Session, userinfo_id: int):
    db_userinfo = get_by_id(db, userinfo_id)
    db.delete(db_userinfo)
    db.commit()
