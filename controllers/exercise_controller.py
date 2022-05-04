from fastapi import APIRouter
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
from services import exercise_service as service
from schemes import exercise_cheme as scheme

app = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/exercise/{exercise_id}", response_model=scheme.Exercise)
def get_exercise(exercise_id: int, db: Session = Depends(get_db)):
    db_exercise = service.get_by_id(db, exercise_id=exercise_id)
    if db_exercise is None:
        raise HTTPException(status_code=404, detail="Exercise not found")
    return db_exercise


@app.get("/exercise")
def get_all_exercise(db: Session = Depends(get_db)):
    return service.get_all(db)


@app.post("/exercise", response_model=scheme.Exercise)
def create_exercise(exercise: scheme.ExerciseBase, db: Session = Depends(get_db)):
    return service.create(db=db, exercise=exercise)


@app.put("/exercise/{exercise_id}", response_model=scheme.Exercise)
def update_exercise(exercise_id: int, exercise: scheme.ExerciseBase, db: Session = Depends(get_db)):
    db_exercise = service.get_by_id(db, exercise_id=exercise_id)
    if db_exercise is None:
        raise HTTPException(status_code=404, detail="Exercise not found")
    return service.update(db=db, exercise_id=exercise_id, exercise=exercise)


@app.put("/exercise/{exercise_id}", response_model=scheme.Exercise)
def update_exercise(exercise_id: int, exercise: scheme.ExerciseBase, db: Session = Depends(get_db)):
    db_exercise = service.get_by_id(db, exercise_id=exercise_id)
    if db_exercise is None:
        raise HTTPException(status_code=404, detail="Exercise not found")
    return service.update(db=db, exercise_id=exercise_id, exercise=exercise)


@app.delete("/exercise/{exercise_id}", response_model=scheme.Exercise)
def delete_article(exercise_id: int, db: Session = Depends(get_db)):
    db_exercise = service.get_by_id(db, exercise_id=exercise_id)
    if db_exercise is None:
        raise HTTPException(status_code=404, detail="Exercise not found")
    return service.delete(db=db, exercise_id=exercise_id)
