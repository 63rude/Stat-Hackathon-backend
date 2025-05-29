import h2o
from h2o.frame import H2OFrame
import pandas as pd

# Initialize H2O once
h2o.init()

# Load trained model
model = h2o.load_model("models/StackedEnsemble_AllModels_3_AutoML_4_20250529_205741")

def interpret_stage(stage):
    stage_str = str(int(float(stage)))  # Handles 4, 4.0, "4"
    return {
        "1": "Minimal fibrosis",
        "2": "Mild fibrosis",
        "3": "Moderate fibrosis",
        "4": "Advanced fibrosis or cirrhosis"
    }.get(stage_str, "Unknown stage")

def predict_stage(input_data: dict):
    try:
        # Convert input to one-row H2OFrame
        formatted = {k: [v] for k, v in input_data.items()}
        frame = H2OFrame(formatted)

        # Ensure categorical variables are marked correctly
        for col in ["Sex", "Ascites", "Hepatomegaly", "Spiders", "Edema"]:
            frame[col] = frame[col].asfactor()

        # Predict
        prediction = model.predict(frame)

        # Handle possible list vs. DataFrame returns
        raw = prediction.as_data_frame()
        if isinstance(raw, list):
            raw_df = pd.DataFrame(raw)
        else:
            raw_df = raw

        # Extract all columns (class + probabilities)
        result = raw_df.iloc[0].to_dict()
        predicted_stage = result.get("predict", "Unknown")

        return {
            "Stage": predicted_stage,
            "Interpretation": interpret_stage(str(predicted_stage)),
            "Probabilities": {k: v for k, v in result.items() if k != "predict"},
            "RawPrediction": result
        }

    except Exception as e:
        print("🔥 Prediction error:", e)
        return {"error": str(e)}
