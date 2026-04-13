import requests # type: ignore
import time

def get_cryptocurrency(crypto, currency):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies={currency}"
    
    response = requests.get(url)

    if response.status_code != 200:
        print("Error:", response.text)
        return None

    data = response.json()

    if crypto not in data:
        print("Invalid cryptocurrency name")
        return None

    return data[crypto][currency]


def take_action(crypto, current_price, alert_price):
    if current_price < alert_price:
        print(f"📉 BUY SIGNAL: {crypto} at {current_price}")

    elif current_price > alert_price:
        print(f"📈 SELL SIGNAL: {crypto} at {current_price}")

    else:
        print("⚖️ Price equals alert")


def price_change_indicator(current_price, alert_price, crypto):
    diff = abs(current_price - alert_price)

    if current_price < alert_price:
        print(f"{crypto} is ₹{diff} below alert price ⬇️")

    elif current_price > alert_price:
        print(f"{crypto} is ₹{diff} above alert price ⬆️")

    else:
        print("Exact match 🎯")

if __name__ == "__main__":
    crypto = input("Enter crypto (bitcoin/ethereum): ").lower()
    currency = input("Enter currency (inr/usd/aed): ").lower()
    alert_price = float(input("Enter alert price: "))

    print("\nTracking started... (Ctrl+C to stop)\n")

    while True:
        price = get_cryptocurrency(crypto, currency)

        if price:
            print(f"\nCurrent Price: ₹{price}")

            take_action(crypto, price, alert_price)
            price_change_indicator(price, alert_price, crypto)

        time.sleep(10)