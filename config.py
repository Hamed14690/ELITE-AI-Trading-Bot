import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

BASE_URL = "https://api.binance.com"

# العملات التي يبدأ البوت بفحصها
SYMBOLS = [
    "BTCUSDT",
    "ETHUSDT",
    "BNBUSDT",
    "SOLUSDT"
]

# وضع التشغيل
# TEST = تحليل فقط
# LIVE = تنفيذ أوامر حقيقية
MODE = "TEST"

# إعدادات المخاطرة
RISK_PER_TRADE = 0.01   # 1%

STOP_LOSS = 0.02        # 2%
TAKE_PROFIT = 0.04      # 4%

# الحد الأدنى للثقة قبل اعتبار الفرصة قوية
MIN_CONFIDENCE = 0.75
