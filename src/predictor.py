import joblib

def load_model():
    model = joblib.load('models/weather_model.pkl')
    le_wind = joblib.load('models/label_encoder.pkl')
    return model, le_wind

def predict_rain(model, input_data):
    prediction = model.predict(input_data)[0]
    confidence = max(model.predict_proba(input_data)[0]) * 100
    return prediction, confidence
