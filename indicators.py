import pandas as pd
import ta


def add_indicators(df):

    df["rsi"] = ta.momentum.RSIIndicator(
        df["close"],
        window=14
    ).rsi()

    df["ema20"] = ta.trend.EMAIndicator(
        df["close"],
        window=20
    ).ema_indicator()

    df["ema50"] = ta.trend.EMAIndicator(
        df["close"],
        window=50
    ).ema_indicator()

    macd = ta.trend.MACD(
        df["close"]
    )

    df["macd"] = macd.macd()
    df["macd_signal"] = macd.macd_signal()

    df["volume_avg"] = (
        df["volume"]
        .rolling(20)
        .mean()
    )

    return df


def trend_score(df):

    score = 0

    last = df.iloc[-1]

    if last["close"] > last["ema20"]:
        score += 1

    if last["ema20"] > last["ema50"]:
        score += 1

    if last["macd"] > last["macd_signal"]:
        score += 1

    if last["volume"] > last["volume_avg"]:
        score += 1

    return score / 4
