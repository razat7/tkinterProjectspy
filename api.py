import json
import requests
url = "https://jsonguide.technologychannel.org/quotes.json"

f = requests.get(url)

quotes = json.loads(f.text)
for quote in quotes:
    text = quote['text']
    print(text)

# for i, quote in enumerate(quotes, 1):
#     # text = quote['text']
#     print(f"{i}. {quote}")
