from pydantic import BaseModel


class FoodBase(BaseModel):
    name: str
    description: str
    calories: float
    fat: float
    carbs: float


class Food(FoodBase):
    id: int

    class Config:
        orm_mode = True
