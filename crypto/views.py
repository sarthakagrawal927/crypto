from django.shortcuts import render


def lower_json(json_info):

    if isinstance(json_info, dict):
        for key in list(json_info.keys()):
            if key.islower():
                lower_json(json_info[key])
            else:
                key_lower = key.lower()
                json_info[key_lower] = json_info[key]
                del json_info[key]
                lower_json(json_info[key_lower])

    elif isinstance(json_info, list):
        for item in json_info:
            lower_json(item)


def home(request):
    import environ
    import requests
    import json
    env = environ.Env(DEBUG=(bool, False))
    environ.Env.read_env()

    # Get news
    api_request = requests.get(
        "https://min-api.cryptocompare.com/data/v2/news/?lang=EN&api_key="+env('KEY'))
    api = json.loads(api_request.content)

    # Get prices
    price_request = requests.get(
        "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH&tsyms=RUP&api_key="+env('KEY'))
    price = json.dumps(json.loads(price_request.content), indent=1)
    lower_json(price)
    print(price)

    return render(request, "home.html", {'api': api, 'price': price})
