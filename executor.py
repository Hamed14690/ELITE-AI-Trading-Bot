import time
import hmac
import hashlib
import requests

from config import API_KEY, API_SECRET, BASE_URL


def sign(params):
    query = '&'.join([f"{k}={v}" for k, v in params.items()])
    return hmac.new(
        API_SECRET.encode(),
        query.encode(),
        hashlib.sha256
    ).hexdigest()


def get_price(symbol):
    url = f"{BASE_URL}/api/v3/ticker/price?symbol={symbol}"
    return float(requests.get(url).json()["price"])


def place_order(symbol, side, quantity):

    url = f"{BASE_URL}/api/v3/order"

    timestamp = int(time.time() * 1000)

    params = {
        "symbol": symbol,
        "side": side,
        "type": "MARKET",
        "quantity": quantity,
        "timestamp": timestamp
    }

    params["signature"] = sign(params)

    headers = {
        "X-MBX-APIKEY": API_KEY
    }

    response = requests.post(
        url,
        params=params,
        headers=headers
    )

    return response.json()
