from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime
from database import Base


class UserInfo(Base):
    __tablename__ = "user_info"

    id = Column(Integer, primary_key=True, index=True)
    login = Column(String)


class Exercise(Base):
    __tablename__ = "exercise"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    body_part = Column(String)
    description = Column(String)


class Food(Base):
    __tablename__ = "food"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    calories = Column(Float)
    fat = Column(Float)
    carbs = Column(Float)


class DailyMeals(Base):
    __tablename__ = "daily_meals"

    id = Column(Integer, primary_key=True, index=True)
    user = Column(Integer, ForeignKey("user_info.id"))
    date = Column(DateTime)
    food = Column(Integer, ForeignKey("food.id"))
    mass = Column(Float)


class DailyWorkout(Base):
    __tablename__ = "daily_workout"

    id = Column(Integer, primary_key=True, index=True)
    user = Column(Integer, ForeignKey("user_info.id"))
    date = Column(DateTime)
    exercise = Column(Integer, ForeignKey("exercise.id"))
    amount = Column(Integer)
    repetition = Column(Integer)