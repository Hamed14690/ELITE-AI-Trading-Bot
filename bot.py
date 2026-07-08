import time

from scanner import scan_market, get_candles
from indicators import add_indicators
from ai_engine import analyze_opportunity
from database import create_table, save_signal
from risk_manager import risk_check
from config import MODE


print("🧠 ELITE AI TRADING BOT V12 STARTING...")


create_table()


while True:

    try:

        print("\n🔎 Scanning market...")

        opportunities = scan_market()


        if not opportunities:
            print("No data")
            time.sleep(60)
            continue


        best = opportunities[0]

        symbol = best["symbol"]

        print(
            f"\n⭐ Best Opportunity: {symbol}"
        )


        df = get_candles(symbol)

        df = add_indicators(df)


        analysis = analyze_opportunity(df)


        signal = analysis["signal"]
        confidence = analysis["confidence"]


        price = df["close"].iloc[-1]


        print(
            f"""
📊 {symbol}

Signal:
{signal}

Confidence:
{confidence}%

Price:
{price}

Mode:
{MODE}
"""
        )


        save_signal(
            symbol,
            signal,
            confidence,
            price
        )


        if (
            signal == "STRONG BUY"
            and risk_check(confidence)
        ):

            print(
                "🚀 High Quality Opportunity Found"
            )


            if MODE == "LIVE":

                print(
                    "⚠️ LIVE MODE ENABLED"
                )

            else:

                print(
                    "🧪 TEST MODE - No Real Order"
                )


        else:

            print(
                "⏳ Waiting for better setup"
            )


        time.sleep(300)


    except Exception as e:

        print(
            "ERROR:",
            e
        )

        time.sleep(60)
