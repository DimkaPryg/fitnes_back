from fastapi import APIRouter
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
from services import dailyworkout_service as service
from schemes import dailyworkout_cheme as scheme

app = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/dailyworkout/{dailyworkout_id}", response_model=scheme.DailyWorkout)
def get_dailyworkout(dailyworkout_id: int, db: Session = Depends(get_db)):
    db_dailyworkout = service.get_by_id(db, dailyworkout_id=dailyworkout_id)
    print("hello")
    if db_dailyworkout is None:
        raise HTTPException(status_code=404, detail="DailyWorkout not found")
    return db_dailyworkout


@app.get("/dailyworkout")
def get_all_dailyworkout(db: Session = Depends(get_db)):
    return service.get_all(db)


@app.post("/dailyworkout", response_model=scheme.DailyWorkout)
def create_dailyworkout(dailyworkout: scheme.DailyWorkoutBase, db: Session = Depends(get_db)):
    return service.create(db=db, dailyworkout=dailyworkout)


@app.put("/dailyworkout/{dailyworkout_id}", response_model=scheme.DailyWorkout)
def update_dailyworkout(dailyworkout_id: int, dailyworkout: scheme.DailyWorkoutBase, db: Session = Depends(get_db)):
    db_dailyworkout = service.get_by_id(db, dailyworkout_id=dailyworkout_id)
    if db_dailyworkout is None:
        raise HTTPException(status_code=404, detail="DailyWorkout not found")
    return service.update(db=db, dailyworkout_id=dailyworkout_id, dailyworkout=dailyworkout)


@app.put("/dailyworkout/{dailyworkout_id}", response_model=scheme.DailyWorkout)
def update_dailyworkout(dailyworkout_id: int, dailyworkout: scheme.DailyWorkoutBase, db: Session = Depends(get_db)):
    db_dailyworkout = service.get_by_id(db, dailyworkout_id=dailyworkout_id)
    if db_dailyworkout is None:
        raise HTTPException(status_code=404, detail="DailyWorkout not found")
    return service.update(db=db, dailyworkout_id=dailyworkout_id, dailyworkout=dailyworkout)


@app.delete("/dailyworkout/{dailyworkout_id}", response_model=scheme.DailyWorkout)
def delete_article(dailyworkout_id: int, db: Session = Depends(get_db)):
    db_dailyworkout = service.get_by_id(db, dailyworkout_id=dailyworkout_id)
    if db_dailyworkout is None:
        raise HTTPException(status_code=404, detail="DailyWorkout not found")
    return service.delete(db=db, dailyworkout_id=dailyworkout_id)
