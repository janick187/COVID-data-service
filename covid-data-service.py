from flask import Flask, request, render_template
import requests
import json

app = Flask("covid-data-service")


@app.route('/getCountryStats', methods = ["GET"])
def getCountryStats():
    # your code

    url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"

    # country = input("Type in the country you are interested in: ")

    parameters = {
        "country": request.args.get('country')
        }

    headers = {
        'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
        'x-rapidapi-key': "759ce667bamsh2973be0263e0a10p132f63jsn35e77aafb8c7"
        }

    response = requests.get(url, headers=headers, params=parameters).json()

    updated = response['data']['covid19Stats'][0]['lastUpdate']
    infected = response['data']['covid19Stats'][0]['confirmed']
    deaths = response['data']['covid19Stats'][0]['deaths']
    recovered = response['data']['covid19Stats'][0]['recovered']

    data_dict = {
        'updated' : updated,
        'infected' : infected,
        'deaths' : deaths,
        'recovered' : recovered
        }
        
    json_data = json.dumps(data_dict)

    return json_data
