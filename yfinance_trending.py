import requests

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-trending-tickers"

querystring = {"region":"US"}

headers = {
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
    'x-rapidapi-key': "86bb0847c2msh62ec4f10fcc7ed9p17aea2jsn6b82733f81a1"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)