from pydantic import BaseModel

class PatientData(BaseModel):
    age: float
    bilirubin: float
    albumin: float
    edema: int
    # Add more fields if your model needs them
