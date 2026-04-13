import requests
import time

def get_price(crypto, currency):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies={currency}"
    
    try:
        response = requests.get(url)
        
        if response.status_code != 200:
            print("Error:", response.text)
            return None

        data = response.json()

        if crypto not in data:
            print("Invalid crypto name")
            return None

        return data[crypto][currency]

    except Exception as e:
        print("Network error:", e)
        return None


# mode 1: 10-minute comparison
def trader_mode(crypto, currency):
    print("\n⏱️ Trader Mode: Checking 10-minute price movement...\n")

    price_0 = get_price(crypto, currency)

    if price_0 is None:
        return

    print(f"Initial Price: ₹{price_0}")

    print("Waiting 10 minutes...\n")
    time.sleep(600)  # 10 minutes

    price_10 = get_price(crypto, currency)

    if price_10 is None:
        return

    print(f"Price after 10 minutes: ₹{price_10}")

    if price_10 == price_0:
        print("⚖️ No change in current price")
    else:
        print("📈 Price changed!")


# mode 2: 12-hour monitoring
def monitor_mode(crypto, currency, alert_price):
    print("\n📊 Monitor Mode: Updates every 12 hours (Ctrl+C to stop)\n")

    while True:
        price = get_price(crypto, currency)

        if price:
            print(f"\nCurrent Price: ₹{price}")

            if price < alert_price:
                print("📉 Below your alert price")
            elif price > alert_price:
                print("📈 Above your alert price")
            else:
                print("⚖️ Equal to alert price")

        print("\nNext update in 12 hours...\n")
        time.sleep(43200)  # 12 hours


if __name__ == "__main__":
    crypto = input("Enter crypto: ").lower()
    currency = input("Enter currency: ").lower()

    print("\nSelect Mode:")
    print("1. Trader Mode (10 min comparison)")
    print("2. Monitor Mode (12 hour updates)")

    choice = input("Enter choice (1/2): ")

    if choice == "1":
        trader_mode(crypto, currency)

    elif choice == "2":
        alert_price = float(input("Enter alert price: "))
        monitor_mode(crypto, currency, alert_price)

    else:
        print("Invalid choice")