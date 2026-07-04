import requests

TELEGRAM_TOKEN = "NEW_TOKEN_HERE"
CHAT_ID = "417209770"

URL = "https://api.metals.live/v1/spot/silver"

LOW = 70
HIGH = 80

def send(msg):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

def get_price():
    r = requests.get(URL).json()
    print(r)

    if not r or "price" not in r[0]:
        raise Exception("Invalid API response")

    return float(r[0]["price"])

price = get_price()

if price <= LOW:
    send(f"🔵 LOW ALERT: {price}")
elif price >= HIGH:
    send(f"🔴 HIGH ALERT: {price}")
else:
    print("OK:", price)
