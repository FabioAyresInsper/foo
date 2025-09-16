from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_prediction():
    return {"message": "This is a prediction service."}
