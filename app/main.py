from fastapi import FastAPI
from app.schemas import PatientData
from app.model import predict_stage

app = FastAPI()

@app.post("/predict")
def predict(data: PatientData):
    input_data = data.dict()
    result = predict_stage(input_data)
    return {"prediction": result}
