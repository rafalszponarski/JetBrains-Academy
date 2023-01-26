from requests import get
from json import loads


currency = input().lower()
page = loads(get(f"http://www.floatrates.com/daily/{currency}.json").text)

cache = {}
if currency == 'usd':
    cache['eur'] = page['eur']['rate']
elif currency == 'eur':
    cache['usd'] = page['usd']['rate']
else:
    cache['eur'] = page['eur']['rate']
    cache['usd'] = page['usd']['rate']

while True:
    exchange = input().lower()
    if not exchange:
        break

    conicoins = float(input())

    print("Checking the cache...")
    if exchange in cache.keys():
        print("Oh! It is in the cache!")
        print(f"You received {round(cache[exchange] * conicoins, 2)} {exchange.upper()}.")

    else:
        print("Sorry, but it is not in the cache!")
        cache[exchange] = page[exchange]["rate"]
        print(f"You received {round(cache[exchange] * conicoins, 2)} {exchange.upper()}.")
