import requests

TELEGRAM_TOKEN = "8845119426:AAEd8BW50q6yKz4K-8tz4D7ABi-lFlRoo5Y"
CHAT_ID = "417209770"

URL = "https://api.metals.live/v1/spot/silver"

LOW = 70
HIGH = 80

def send(msg):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

def get_price():
    r = requests.get(URL).json()
    return float(r[0]["price"])

price = get_price()

if price <= LOW:
    send(f"🔵 LOW ALERT: {price}")
elif price >= HIGH:
    send(f"🔴 HIGH ALERT: {price}")
else:
    print("OK:", price)
