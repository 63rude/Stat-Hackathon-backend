import h2o
from h2o.frame import H2OFrame

# Start H2O (once per app)
h2o.init()

# Load your trained model
model = h2o.load_model("models/StackedEnsemble_AllModels_3_AutoML_4_20250529_205741")

def predict_stage(input_data: dict):
    # Convert input dict to H2OFrame
    frame = H2OFrame([input_data])

    # Make prediction
    prediction = model.predict(frame)

    # Convert to Python dict
    return prediction.as_data_frame().to_dict(orient="records")[0]
