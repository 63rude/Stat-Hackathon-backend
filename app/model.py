import h2o
from h2o.frame import H2OFrame
import pandas as pd
from pathlib import Path

# Initialize H2O once
h2o.init()

# Load trained model
model_path = Path(__file__).resolve().parent.parent / "models" / "StackedEnsemble_AllModels_3_AutoML_4_20250529_205741"
model = h2o.load_model(str(model_path))

def interpret_stage(stage):
    stage_str = str(int(float(stage)))  # Handles 4, 4.0, "4"
    return {
        "1": "Minimal fibrosis",
        "2": "Mild fibrosis",
        "3": "Moderate fibrosis",
        "4": "Advanced fibrosis or cirrhosis"
    }.get(stage_str, "Unknown stage")

def predict_stage(input_data: dict):
    # Keep calculated features in sync with the values entered in the form.
    input_data = dict(input_data)
    input_data["SGOTxALKPHOS"] = input_data["SGOT"] * input_data["Alk_Phos"]
    input_data["SGOTxBILIRUBIN"] = input_data["SGOT"] * input_data["Bilirubin"]

    formatted = {k: [v] for k, v in input_data.items()}
    frame = H2OFrame(formatted)

    for col in ["Sex", "Ascites", "Hepatomegaly", "Spiders", "Edema"]:
        frame[col] = frame[col].asfactor()

    prediction = model.predict(frame)

    raw = prediction.as_data_frame()
    raw_df = pd.DataFrame(raw) if isinstance(raw, list) else raw

    result = raw_df.iloc[0].to_dict()
    predicted_stage = result.get("predict", "Unknown")

    return {
        "Stage": predicted_stage,
        "Interpretation": interpret_stage(str(predicted_stage)),
        "Probabilities": {k: v for k, v in result.items() if k != "predict"},
        "RawPrediction": result,
    }
