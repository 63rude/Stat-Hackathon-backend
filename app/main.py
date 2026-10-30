import logging
import os

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import PatientData
from app.model import predict_stage

app = FastAPI()

allowed_origins = os.environ.get(
    "CORS_ORIGINS", "http://localhost:5173,http://127.0.0.1:5173"
).split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin.strip() for origin in allowed_origins if origin.strip()],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict")
def predict(data: PatientData):
    try:
        return {"prediction": predict_stage(data.model_dump(exclude_none=True))}
    except Exception:
        logging.exception("Prediction failed")
        raise HTTPException(status_code=500, detail="Prediction failed; check the server logs")
