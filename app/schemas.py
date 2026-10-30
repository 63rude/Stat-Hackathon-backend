from pydantic import BaseModel
from typing import Literal

class PatientData(BaseModel):
    Age: float
    Sex: Literal["F", "M"]
    Ascites: Literal["N", "Y"]
    Hepatomegaly: Literal["N", "Y"]
    Spiders: Literal["N", "Y"]
    Edema: Literal["N", "S", "Y"]
    Bilirubin: float
    Cholesterol: float
    Albumin: float
    Copper: float
    Alk_Phos: float
    SGOT: float
    Tryglicerides: float
    Platelets: float
    Prothrombin: float
    SGOTxALKPHOS: float | None = None
    SGOTxBILIRUBIN: float | None = None
