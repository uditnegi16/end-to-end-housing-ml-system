from fastapi import FastAPI
from app.schemas import HousingRequest
from src.predict import predict_price
from src.investment_decision import make_investment_decision
from src.monitor import log_prediction
import time 
app=FastAPI(title="end-to-end hosuing ml system")

@app.get("/")
def home():
    return {"status":"running",
            "message":"Housing ML Api is live.Go to /docs to test prediction0"
            }

@app.post("/predict")
def predict(data: HousingRequest):
    start_time = time.time()

    input_data = data.model_dump()
    predicted_price = predict_price(input_data)
    decision = make_investment_decision(predicted_price)

    latency_ms = round((time.time() - start_time) * 1000, 2)

    log_prediction(input_data, predicted_price, decision, latency_ms)

    return {
        "predicted_price": round(predicted_price, 2),
        **decision,
        "latency_ms": latency_ms
    }