from sqlalchemy.orm import Session
from schemes import food_cheme as scheme
import models


def get_by_id(db: Session, food_id: int):
    return db.query(models.Food).filter(models.Food.id == food_id).first()


def get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Food).offset(skip).limit(limit).all()


def create(db: Session, food: scheme.FoodBase):
    db_food = models.Food(name=food.name, description=food.description, calories=food.calories, carbs=food.carbs,
                          fat=food.fat)
    db.add(db_food)
    db.commit()
    db.refresh(db_food)
    return db_food


def update(db: Session, food_id: int, food: scheme.FoodBase):
    db_food = get_by_id(db, food_id)
    db_food.name = food.name
    db_food.description = food.description
    db_food.calories = food.calories
    db_food.carbs = food.carbs
    db_food.fat = food.fat
    db.commit()
    db.refresh(db_food)
    return db_food


def delete(db: Session, food_id: int):
    db_food = get_by_id(db, food_id)
    db.delete(db_food)
    db.commit()
