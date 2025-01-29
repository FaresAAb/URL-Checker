import pickle
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template

# Load the trained model
with open("phishing_model.pkl", "rb") as f:
    model = pickle.load(f)

# Load dataset column names
df = pd.read_csv("Cleaned_Merged_Dataset.csv")
feature_columns = df.drop(columns=["CLASS_LABEL"]).columns.tolist()  # Ensure correct feature order

# Initialize Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        url = data.get("url")

        if not url:
            return jsonify({"error": "URL is required"}), 400

        # Feature Extraction
        url_features = {
            "NumDots": url.count("."),
            "SubdomainLevel": url.count(".") - 1,
            "PathLevel": url.count("/"),
            "UrlLength": len(url),
            "NumDash": url.count("-"),
            "NumDashInHostname": url.split("/")[2].count("-") if "/" in url else 0,
            "AtSymbol": 1 if "@" in url else 0,
            "TildeSymbol": 1 if "~" in url else 0,
            "NumUnderscore": url.count("_"),
            "NumPercent": url.count("%"),
            "NumQueryComponents": url.count("?"),
            "NumAmpersand": url.count("&"),
            "NumHash": url.count("#"),
            "NumNumericChars": sum(c.isdigit() for c in url),
            "NoHttps": 1 if not url.startswith("https") else 0,
            "SuspiciousKeyword": 1 if any(word in url.lower() for word in ["secure", "login", "verify", "update", "bank", "confirm", "auth", "signin", "account"]) else 0
        }

        # Debugging: Print extracted features
        print("\n🔍 Extracted Features for Debugging:", url_features)

        # Convert to DataFrame for model input
        input_data = pd.DataFrame([url_features], columns=feature_columns)

        # Predict using the trained model
        prediction = model.predict(input_data)[0]
        result = "Phishing" if prediction == 1 else "Legitimate"

        print(f"🔍 Model Prediction: {result}")
        return jsonify({"prediction": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
