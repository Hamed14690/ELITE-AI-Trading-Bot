import requests
import pandas as pd

from config import BASE_URL, SYMBOLS
from indicators import add_indicators, trend_score


def get_candles(symbol, interval="15m", limit=100):

    url = (
        f"{BASE_URL}/api/v3/klines"
        f"?symbol={symbol}"
        f"&interval={interval}"
        f"&limit={limit}"
    )

    data = requests.get(url).json()

    df = pd.DataFrame(data, columns=[
        "time",
        "open",
        "high",
        "low",
        "close",
        "volume",
        "close_time",
        "qav",
        "trades",
        "tbbav",
        "tbqav",
        "ignore"
    ])

    df["close"] = df["close"].astype(float)
    df["volume"] = df["volume"].astype(float)

    return df


def scan_market():

    results = []

    for symbol in SYMBOLS:

        try:
            df = get_candles(symbol)

            df = add_indicators(df)

            score = trend_score(df)

            results.append({
                "symbol": symbol,
                "score": round(score, 2),
                "price": df["close"].iloc[-1]
            })

        except Exception as e:
            print(symbol, e)

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results


if __name__ == "__main__":

    opportunities = scan_market()

    for item in opportunities:
        print(item)
