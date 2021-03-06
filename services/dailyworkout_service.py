from sqlalchemy.orm import Session
from schemes import dailyworkout_cheme as scheme
from datetime import datetime
import models


def get_by_id(db: Session, dailyworkout_id: int):
    return db.query(models.DailyWorkout).filter(models.DailyWorkout.id == dailyworkout_id).first()


def get_by_date(db: Session, date: datetime):
    return db.query(models.DailyWorkout).filter(models.DailyWorkout.date == date).all()


def get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.DailyWorkout).offset(skip).limit(limit).all()


def create(db: Session, dailyworkout: scheme.DailyWorkoutCreate):
    db_dailyworkout = models.DailyWorkout(user_id=dailyworkout.user_id, date=dailyworkout.date,
                                          exercise_id=dailyworkout.exercise_id,
                                          amount=dailyworkout.amount, repetition=dailyworkout.repetition)
    db.add(db_dailyworkout)
    db.commit()
    db.refresh(db_dailyworkout)
    return db_dailyworkout


def update(db: Session, dailyworkout_id: int, dailyworkout: scheme.DailyWorkoutCreate):
    db_dailyworkout = get_by_id(db, dailyworkout_id)
    db_dailyworkout.user_id = dailyworkout.user_id
    db_dailyworkout.date = dailyworkout.date
    db_dailyworkout.exercise_id = dailyworkout.exercise_id
    db_dailyworkout.amount = dailyworkout.amount
    db_dailyworkout.repetition = dailyworkout.repetition
    db.commit()
    db.refresh(db_dailyworkout)
    return db_dailyworkout


def delete(db: Session, dailyworkout_id: int):
    db_dailyworkout = get_by_id(db, dailyworkout_id)
    db.delete(db_dailyworkout)
    db.commit()
