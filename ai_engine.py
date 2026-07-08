from indicators import trend_score


def analyze_opportunity(df):

    score = trend_score(df)

    rsi = df["rsi"].iloc[-1]
    macd = df["macd"].iloc[-1]
    macd_signal = df["macd_signal"].iloc[-1]

    confidence = score


    # RSI analysis
    if 40 < rsi < 70:
        confidence += 0.10

    elif rsi > 75:
        confidence -= 0.10


    # MACD confirmation
    if macd > macd_signal:
        confidence += 0.10
    else:
        confidence -= 0.05


    # keep range
    if confidence > 1:
        confidence = 1

    if confidence < 0:
        confidence = 0


    if confidence >= 0.80:
        signal = "STRONG BUY"

    elif confidence >= 0.65:
        signal = "BUY CONFIRMATION"

    elif confidence >= 0.45:
        signal = "WAIT"

    else:
        signal = "AVOID"


    return {
        "signal": signal,
        "confidence": round(confidence * 100, 2)
    }
