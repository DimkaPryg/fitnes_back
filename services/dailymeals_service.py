from sqlalchemy.orm import Session
from schemes import dailymeals_cheme as scheme
import models


def get_by_id(db: Session, dailymeals_id: int):
    return db.query(models.DailyMeals).filter(models.DailyMeals.id == dailymeals_id).first()


def get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.DailyMeals).offset(skip).limit(limit).all()


def create(db: Session, dailymeals: scheme.DailyMealsBase):
    db_dailymeals = models.DailyMeals(user=dailymeals.user, date=dailymeals.date, food=dailymeals.food,
                                      mass=dailymeals.mass)
    db.add(db_dailymeals)
    db.commit()
    db.refresh(db_dailymeals)
    return db_dailymeals


def update(db: Session, dailymeals_id: int, dailymeals: scheme.DailyMealsBase):
    db_dailymeals = get_by_id(db, dailymeals_id)
    db_dailymeals.user = dailymeals.user
    db_dailymeals.date = dailymeals.date
    db_dailymeals.food = dailymeals.food
    db_dailymeals.mass = dailymeals.mass
    db.commit()
    db.refresh(db_dailymeals)
    return db_dailymeals


def delete(db: Session, dailymeals_id: int):
    db_dailymeals = get_by_id(db, dailymeals_id)
    db.delete(db_dailymeals)
    db.commit()
