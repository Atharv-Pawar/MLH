import requests
import random

def get_joke():
    url = "https://v2.jokeapi.dev/joke/Any"
    response = requests.get(url)

    if response.status_code != 200:
        return "Error fetching joke"

    data = response.json()

    if data["type"] == "single":
        return data["joke"]
    else:
        return f"{data['setup']}\n{data['delivery']}"


def get_quote():
    url = "https://zenquotes.io/api/random"
    response = requests.get(url)

    if response.status_code != 200:
        return "Error fetching quote"

    data = response.json()
    return f"{data[0]['q']} - {data[0]['a']}"


def surprise():
    choice = random.choice(["joke", "quote"])

    if choice == "joke":
        print("\n😂 Here's a joke:\n")
        print(get_joke())
    else:
        print("\n💬 Here's a quote:\n")
        print(get_quote())


# MAIN
print("1. Get Joke")
print("2. Get Quote")
print("3. Surprise Me 🎲")

choice = input("Enter choice: ")

if choice == "1":
    print("\n😂 Joke:\n")
    print(get_joke())

elif choice == "2":
    print("\n💬 Quote:\n")
    print(get_quote())

elif choice == "3":
    surprise()

else:
    print("Invalid choice")