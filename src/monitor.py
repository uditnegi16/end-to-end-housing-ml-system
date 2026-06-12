import json
import time
from pathlib import Path

LOG_PATH = Path("logs/predictions.log")


def log_prediction(input_data: dict, prediction: float, decision: dict, latency_ms: float):
    LOG_PATH.parent.mkdir(exist_ok=True)

    record = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "input": input_data,
        "predicted_price": prediction,
        "decision": decision,
        "latency_ms": latency_ms
    }

    with open(LOG_PATH, "a") as f:
        f.write(json.dumps(record) + "\n")