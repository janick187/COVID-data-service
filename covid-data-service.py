from flask import Flask, request, Response, render_template
import requests
import json

app = Flask(__name__)

@app.route('/getCountryStats', methods = ["GET"])
def getCountryStats():
    # your code

    url = "https://covidapi.info/api/v1/country/{}/latest".format(request.args.get('country'))

    response = requests.get(url)
    
    if response.status_code == 200:
        
        data =response.json()
        
        date = list(data['result'].items())[0][0]

        infected = data['result'][date]['confirmed']
        deaths = data['result'][date]['deaths']
        recovered = data['result'][date]['recovered']
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

    else:
       
       resp = Response(status=404)
    
    resp.headers['Access-Control-Allow-Origin'] = '*'
    
    return resp