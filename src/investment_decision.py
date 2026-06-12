def make_investment_decision(predicted_price:float):
    if predicted_price<=250000:
        return {
            "decision":"INVEST",
            "risk_level":"LOW"
        }
    elif predicted_price<=400000:
        return{
            "decision":"INVEST",
            "risk_level":"MEDIUM"
        }
    return{
        "decision":"DO_NOT_INVEST",
        "risk_level":"HIGH"
    }