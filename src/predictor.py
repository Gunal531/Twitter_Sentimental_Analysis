import joblib
import os

# Load model from the workspace root
model_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'sentiment_model.pkl')
model = joblib.load(model_path)

def predict_sentiment(text):
    prediction = model.predict([text])[0]
    
    # Map numeric prediction to sentiment label
    if prediction == 1.0:
        return "positive"
    elif prediction == -1.0:
        return "negative"
    else:
        return "neutral"