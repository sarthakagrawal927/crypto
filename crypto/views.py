from django.shortcuts import render
import environ
import requests
import json
env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env()


def home(request):

    # Get news
    api_request = requests.get(
        "https://min-api.cryptocompare.com/data/v2/news/?lang=EN&api_key="+env('KEY'))
    api = json.loads(api_request.content)

    # Get prices
    price_request = requests.get(
        "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,LTC,ADA,BCH,XRP,DOGE&tsyms=RUP&api_key="+env('KEY'))
    price = json.loads(price_request.content)

    return render(request, "home.html", {'api': api, 'price': price})


def prices(request):
    if request.method == 'POST':
        quote = request.POST['quote']
        quote = quote.upper()
        crypto_request = requests.get(
            "https://min-api.cryptocompare.com/data/pricemultifull?fsyms="+quote+"&tsyms=RUP&api_key="+env('KEY'))
        crypto = json.loads(crypto_request.content)
        return render(request, 'prices.html', {'quote': quote, 'crypto': crypto})

    notFound = "Enter a valid cryptocurrencyadasd"
    return render(request, "prices.html", {'notFound': notFound})
