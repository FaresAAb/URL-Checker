# Phishing URL Checker

## Overview
This project is a **Phishing URL Checker** that utilizes a **Machine Learning model** to predict whether a given URL is **Legitimate** or **Phishing**. It is built using **Python, Flask, and RandomForestClassifier** and provides a web-based interface for easy testing.

## Features
- **Trained Machine Learning Model:** Uses a RandomForest classifier for phishing detection.
- **Web-based Interface:** A user-friendly site to input and analyze URLs.
- **REST API Endpoint:** Allows programmatic access to predictions.
- **Custom Feature Extraction:** Extracts meaningful attributes from URLs.

## Project Structure
```
📂 phishing-url-checker
├── 📄 train_model.py    # ML Model Training Script
├── 📄 app.py           # Flask Backend API
├── 📄 index.html       # Frontend Interface
├── 📄 requirements.txt # Dependencies
├── 📄 phishing_model.pkl # Saved ML Model
├── 📄 static/          # Static assets (CSS, JS, Images)
└── 📄 templates/       # HTML Templates
```

## Setup Instructions
### 1. Clone the Repository
```sh
git clone https://github.com/yourusername/phishing-url-checker.git
cd phishing-url-checker
```

### 2. Install Dependencies
Ensure you have **Python 3.x** installed, then run:
```sh
pip install -r requirements.txt
```

### 3. Train the Model
Run the following command to train the **RandomForestClassifier** model using the dataset:
```sh
python train_model.py
```
This will generate a **phishing_model.pkl** file, which will be used for predictions.

### 4. Start the Flask App
Launch the Flask web server with:
```sh
python app.py
```
By default, the app will run at:
```
http://127.0.0.1:5000/
```

## Using the Web Interface
1. Open **http://127.0.0.1:5000/** in your browser.
2. Enter a URL in the input field.
3. Click the **"Check"** button.
4. The system will analyze the URL and return one of the following:
   - ✅ **Legitimate** if the URL is safe.
   - 🚨 **Phishing** if the URL is suspicious.

## Testing via API
### **Postman or cURL**
#### **Endpoint:**
```
POST /predict
```
#### **Request Body:**
```json
{
  "url": "http://secure-login-update.com"
}
```
#### **Response Example:**
```json
{
  "prediction": "Phishing"
}
```
#### **cURL Command:**
```sh
curl -X POST "http://127.0.0.1:5000/predict" \
     -H "Content-Type: application/json" \
     -d '{"url":"http://secure-login-update.com"}'
```

## Dataset
- The project uses **Cleaned_Merged_Dataset.csv**, which contains labeled phishing and legitimate URLs.
- Feature extraction includes elements like `NumDots`, `SubdomainLevel`, `UrlLength`, `NumDash`, etc.

## Deployment (Optional)
To deploy the Flask app on a server:
```sh
pip install gunicorn
```
Run the server:
```sh
gunicorn --bind 0.0.0.0:5000 app:app
```
For Docker deployment:
1. Build the Docker image:
   ```sh
   docker build -t phishing-checker .
   ```
2. Run the container:
   ```sh
   docker run -p 5000:5000 phishing-checker
   ```

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to improve.

## License
This project is licensed under fares

## Contact
For any issues or questions, feel free to reach out via fares1aa@hotmail.com or open an issue in the repository.

---
**Happy Coding! 🚀**

