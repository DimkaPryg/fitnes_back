from pydantic import BaseModel


class ExerciseBase(BaseModel):
    name: str
    body_part: str
    description: str


class Exercise(ExerciseBase):
    id: int

    class Config:
        orm_mode = True