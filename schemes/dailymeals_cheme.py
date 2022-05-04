from datetime import datetime

from pydantic import BaseModel

from schemes.food_cheme import Food
from schemes.userinfo_scheme import UserInfo


class DailyMealsBase(BaseModel):
    user: UserInfo
    date: datetime
    food: Food
    mass: float


class DailyMeals(DailyMealsBase):
    id: int

    class Config:
        orm_mode = True
