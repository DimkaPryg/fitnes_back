from sqlalchemy.orm import Session
from schemes import exercise_cheme as scheme
import models


def get_by_id(db: Session, exercise_id: int):
    return db.query(models.Exercise).filter(models.Exercise.id == exercise_id).first()


def get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Exercise).offset(skip).limit(limit).all()


def create(db: Session, exercise: scheme.ExerciseBase):
    db_exercise = models.Exercise(name=exercise.name, body_part=exercise.body_part, description=exercise.description)
    db.add(db_exercise)
    db.commit()
    db.refresh(db_exercise)
    return db_exercise


def update(db: Session, exercise_id: int, exercise: scheme.ExerciseBase):
    db_exercise = get_by_id(db, exercise_id)
    db_exercise.name = exercise.name
    db_exercise.body_part = exercise.body_part
    db_exercise.description = exercise.description
    db.commit()
    db.refresh(db_exercise)
    return db_exercise


def delete(db: Session, exercise_id: int):
    db_exercise = get_by_id(db, exercise_id)
    db.delete(db_exercise)
    db.commit()