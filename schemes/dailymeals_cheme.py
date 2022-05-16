from datetime import datetime
from typing import Union, Optional
from pydantic import BaseModel

from schemes.food_cheme import Food, FoodBase
from schemes.userinfo_scheme import UserInfo, UserInfoBase


class DailyMealsBase(BaseModel):
    user: Union[UserInfo, None] = None
    date: datetime
    food: Union[Food, None] = None
    mass: float


class DailyMeals(DailyMealsBase):
    id: int

    class Config:
        orm_mode = True
