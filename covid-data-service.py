from flask import Flask, request, Response, render_template
import requests
import json

app = Flask(__name__)

@app.route('/getCountryStats', methods = ["GET"])
def getCountryStats():
    # your code

    url = "https://covidapi.info/api/v1/country/{}/latest".format(request.args.get('country'))

    response = requests.get(url).json()

    date = list(response['result'].items())[0][0]

    infected = response['result'][date]['confirmed']
    deaths = response['result'][date]['deaths']
    recovered = response['result'][date]['recovered']
    mortality = round((deaths * 100) / infected, 2)

    data_dict = {
        'updated' : date,
        'infected' : infected,
        'deaths' : deaths,
        'recovered' : recovered,
        'mortality' : mortality
        }
        
    json_data = json.dumps(data_dict)

    resp = Response(json_data)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    
    return resp