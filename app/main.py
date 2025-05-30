from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import PatientData
from app.model import predict_stage

app = FastAPI()

app = FastAPI()

# 👇 Add this block
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:5173"] for local frontend only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict")
def predict(data: PatientData):
    input_data = data.dict()
    result = predict_stage(input_data)
    return {"prediction": result}
