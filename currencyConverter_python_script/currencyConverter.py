import requests
API_KEY = 'fca_live_kHFm435xYz39QrKYRBiopijs1tlPQnG0qz8yC3qa'
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD","AUD","EUR","KRW","INR","CAD"]

def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"

    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]

    except Exception as e:
        print("Invalid Currency!")
        return None

def convert_amount(amount, base, target):
    data = convert_currency(base)
    if not data:
        return None

    base_rate = data[base]
    target_rate = data[target]

    converted_amount = amount*(target_rate/base_rate)
    return converted_amount



while True:
    base = input("Enter the base currency (q for quit): ").upper()
   # base_value_multiplier = int(input("Enter the amount you want to convert(or q for quit): "))

    if base == "Q":
        break
        
    data = convert_currency(base)

    if not data:
        continue
    
    del data[base]

    for ticker, value in data.items():
        print(f"{ticker}: {value}")   

    target_currency = input("Enter the target currency to convert amount: ").upper()
    amount = float(input("Enter the amount you want to convert: ")) 

    converted_amount = convert_amount(amount,base,target_currency)
    if converted_amount is not None:
        print(f"{amount} {base} is equal to {converted_amount} {target_currency}")   
