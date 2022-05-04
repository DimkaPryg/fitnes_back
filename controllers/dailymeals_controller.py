from fastapi import APIRouter
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
from services import dailymeals_service as service
from schemes import dailymeals_cheme as scheme

app = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/dailymeals/{dailymeals_id}", response_model=scheme.DailyMeals)
def get_dailymeals(dailymeals_id: int, db: Session = Depends(get_db)):
    db_dailymeals = service.get_by_id(db, dailymeals_id=dailymeals_id)
    if db_dailymeals is None:
        raise HTTPException(status_code=404, detail="DailyMeals not found")
    return db_dailymeals


@app.get("/dailymeals")
def get_all_dailymeals(db: Session = Depends(get_db)):
    return service.get_all(db)


@app.post("/dailymeals", response_model=scheme.DailyMeals)
def create_dailymeals(dailymeals: scheme.DailyMealsBase, db: Session = Depends(get_db)):
    return service.create(db=db, dailymeals=dailymeals)


@app.put("/dailymeals/{dailymeals_id}", response_model=scheme.DailyMeals)
def update_dailymeals(dailymeals_id: int, dailymeals: scheme.DailyMealsBase, db: Session = Depends(get_db)):
    db_dailymeals = service.get_by_id(db, dailymeals_id=dailymeals_id)
    if db_dailymeals is None:
        raise HTTPException(status_code=404, detail="DailyMeals not found")
    return service.update(db=db, dailymeals_id=dailymeals_id, dailymeals=dailymeals)


@app.put("/dailymeals/{dailymeals_id}", response_model=scheme.DailyMeals)
def update_dailymeals(dailymeals_id: int, dailymeals: scheme.DailyMealsBase, db: Session = Depends(get_db)):
    db_dailymeals = service.get_by_id(db, dailymeals_id=dailymeals_id)
    if db_dailymeals is None:
        raise HTTPException(status_code=404, detail="DailyMeals not found")
    return service.update(db=db, dailymeals_id=dailymeals_id, dailymeals=dailymeals)


@app.delete("/dailymeals/{dailymeals_id}", response_model=scheme.DailyMeals)
def delete_article(dailymeals_id: int, db: Session = Depends(get_db)):
    db_dailymeals = service.get_by_id(db, dailymeals_id=dailymeals_id)
    if db_dailymeals is None:
        raise HTTPException(status_code=404, detail="DailyMeals not found")
    return service.delete(db=db, dailymeals_id=dailymeals_id)
