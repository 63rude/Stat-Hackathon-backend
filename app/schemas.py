from pydantic import BaseModel

class PatientData(BaseModel):
    Age: float
    Sex: str  # ✅ change from int to str
    Ascites: int
    Hepatomegaly: int
    Spiders: int
    Edema: int
    Bilirubin: float
    Cholesterol: float
    Albumin: float
    Copper: float
    Alk_Phos: float
    SGOT: float
    Tryglicerides: float
    Platelets: float
    Prothrombin: float
    SGOTxALKPHOS: float
    SGOTxBILIRUBIN: float
