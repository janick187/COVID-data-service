import requests

url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"

querystring = {"country":"Switzerland"}

headers = {
    'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
    'x-rapidapi-key': "759ce667bamsh2973be0263e0a10p132f63jsn35e77aafb8c7"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)