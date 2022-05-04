from fastapi import APIRouter
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
from services import food_service as service
from schemes import food_cheme as scheme

app = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/food/{food_id}", response_model=scheme.Food)
def get_food(food_id: int, db: Session = Depends(get_db)):
    db_food = service.get_by_id(db, food_id=food_id)
    if db_food is None:
        raise HTTPException(status_code=404, detail="Food not found")
    return db_food


@app.get("/food")
def get_all_food(db: Session = Depends(get_db)):
    return service.get_all(db)


@app.post("/food", response_model=scheme.Food)
def create_food(food: scheme.FoodBase, db: Session = Depends(get_db)):
    return service.create(db=db, food=food)


@app.put("/food/{food_id}", response_model=scheme.Food)
def update_food(food_id: int, food: scheme.FoodBase, db: Session = Depends(get_db)):
    db_food = service.get_by_id(db, food_id=food_id)
    if db_food is None:
        raise HTTPException(status_code=404, detail="Food not found")
    return service.update(db=db, food_id=food_id, food=food)


@app.put("/food/{food_id}", response_model=scheme.Food)
def update_food(food_id: int, food: scheme.FoodBase, db: Session = Depends(get_db)):
    db_food = service.get_by_id(db, food_id=food_id)
    if db_food is None:
        raise HTTPException(status_code=404, detail="Food not found")
    return service.update(db=db, food_id=food_id, food=food)


@app.delete("/food/{food_id}", response_model=scheme.Food)
def delete_article(food_id: int, db: Session = Depends(get_db)):
    db_food = service.get_by_id(db, food_id=food_id)
    if db_food is None:
        raise HTTPException(status_code=404, detail="Food not found")
    return service.delete(db=db, food_id=food_id)
