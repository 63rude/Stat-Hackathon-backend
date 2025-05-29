import h2o
from h2o.estimators import H2ORandomForestEstimator

# Start H2O server
h2o.init()

# Load dataset
data = h2o.import_file("dataset.csv")

# Set response and features
target = "Stage"
features = [col for col in data.columns if col != target]

# Ensure response column is categorical for classification
data[target] = data[target].asfactor()

# Split into training and testing sets
train, test = data.split_frame(ratios=[0.8], seed=1234)

# Initialize and train the model
model = H2ORandomForestEstimator()
model.train(x=features, y=target, training_frame=train)

# Print the response column used
print("✅ Target column used for training:", target)

# Optional: model performance
perf = model.model_performance(test_data=test)
print(perf)
