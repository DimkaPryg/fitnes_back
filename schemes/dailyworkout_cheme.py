from datetime import datetime
from typing import Union
from pydantic import BaseModel

from schemes.exercise_cheme import Exercise
from schemes.userinfo_scheme import UserInfo


class DailyWorkoutBase(BaseModel):
    user: Union[UserInfo, None] = None
    date: datetime
    exercise: Union[Exercise, None] = None
    amount: int
    repetition: int


class DailyWorkout(DailyWorkoutBase):
    id: int

    class Config:
        orm_mode = True
