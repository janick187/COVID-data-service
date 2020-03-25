from flask import Flask, request, render_template
import requests

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

    json = requests.get(url, headers=headers, params=parameters).json()

    updated = json['data']['covid19Stats'][0]['lastUpdate']
    infected = json['data']['covid19Stats'][0]['confirmed']
    deaths = json['data']['covid19Stats'][0]['deaths']
    recovered = json['data']['covid19Stats'][0]['recovered']

    result_string = "{}\n{}\n{}\n{}".format(updated, infected, deaths, recovered)

    return result_string
