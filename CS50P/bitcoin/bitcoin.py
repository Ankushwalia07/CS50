import sys
import requests

def main():
    if len(sys.argv) == 2:
        try:
            n = float(sys.argv[1])
            convert(n)
        except ValueError:
            sys.exit("Command-line argument is not a number")
    else:
        sys.exit("No command line arguement Found")


def convert(num):
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        obj = response.json()
        rate = obj["bpi"]["USD"]["rate_float"]
        total = num * rate
        print(f"${total:,.4f}")
    except requests.RequestException:
        return None


main()e

