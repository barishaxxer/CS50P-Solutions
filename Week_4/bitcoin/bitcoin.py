import requests
import json
import sys
def main():
    price = get_price()
    if len(sys.argv) == 2:
        try:
            btc,x = float(price.replace(",","")),float(sys.argv[1])
            print(f"${x * btc:,}")
        except ValueError:
            sys.exit("Command-line argument is not a number")
    else:
        sys.exit("Missing command-line argument")

def get_price():
    
    try:
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        return json.loads(r.text)["bpi"]["USD"]["rate"]
    except requests.RequestException:
        pass

main()

