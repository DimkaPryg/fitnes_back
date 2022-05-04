from fastapi import FastAPI
import models
from database import engine
from controllers import userinfo_controller, exercise_controller, food_controller, dailymeals_controller

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(userinfo_controller.app)
app.include_router(exercise_controller.app)
app.include_router(food_controller.app)
app.include_router(dailymeals_controller.app)


@app.get("/cowsay")
def hello_world():
    return "Moo"
