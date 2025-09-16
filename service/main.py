from fastapi import FastAPI
import joblib
from pydantic import BaseModel


class InputData(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float


app = FastAPI()

with open("../best_model.joblib", "rb") as f:
    model = joblib.load(f)


@app.post("/prediction")
def read_prediction(item: InputData):
    prediction = model.predict([list(item.model_dump().values())])[0]
    return {
        "message": "This is a prediction service.",
        "data": item,
        "prediction": prediction,
    }
