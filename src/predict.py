import joblib
import pandas as pd

pipeline = joblib.load("models/full_pipeline.joblib")
model = joblib.load("models/price_model.joblib")


def predict_price(input_data: dict) -> float:
    df = pd.DataFrame([input_data])

    transformed_data = pipeline.transform(df)

    prediction = model.predict(transformed_data)

    return float(prediction[0])
from src.predict import predict_price

print("loaded successfully")
