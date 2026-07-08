from config import (
    RISK_PER_TRADE,
    STOP_LOSS,
    TAKE_PROFIT
)


def calculate_position(balance, price):

    risk_amount = balance * RISK_PER_TRADE

    quantity = risk_amount / (price * STOP_LOSS)

    return round(quantity, 6)


def calculate_levels(entry):

    stop_loss = entry * (1 - STOP_LOSS)

    take_profit = entry * (1 + TAKE_PROFIT)

    return {
        "entry": round(entry, 4),
        "stop_loss": round(stop_loss, 4),
        "take_profit": round(take_profit, 4)
    }


def risk_check(confidence):

    if confidence < 70:
        return False

    return True
