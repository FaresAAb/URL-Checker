import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the dataset
df = pd.read_csv("Cleaned_Merged_Dataset.csv")

# Print column names to check if "CLASS_LABEL" exists
print("Columns in dataset:", df.columns)

# Ensure "CLASS_LABEL" exists, rename if necessary
if "CLASS_LABEL" not in df.columns:
    raise KeyError("The dataset does not contain 'CLASS_LABEL'. Check the column names.")

# Drop unnecessary columns (modify according to your dataset)
columns_to_remove = ["id"] if "id" in df.columns else []
X = df.drop(columns=columns_to_remove + ["CLASS_LABEL"])  
y = df["CLASS_LABEL"]

# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the RandomForest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Save the trained model
with open("phishing_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved as phishing_model.pkl")
