from wsgiref import headers
from flask import Flask
from flask_cors import CORS, cross_origin
import requests

app = Flask(__name__)
cors = CORS(app, resources={"/": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

radiation_cache = dict()

@app.route('/radiations/<latitude>/<longitude>')
@cross_origin(origins='*', headers=['Content_Type', 'Authorization'])
def get_radiation(latitude, longitude):
    if (latitude, longitude) not in radiation_cache.keys():
        request = requests.get(
            f'https://api.meteomatics.com/2022-10-01T00:00:00ZP2D:PT1H/clear_sky_rad:W/{latitude},{longitude}/json',
            auth=('polyorbite_sat', '2h8wO4gE3L')
        )
        data = request.json()
        radiation_cache[(latitude, longitude)] = data
    

    try:
        measurements = radiation_cache[(latitude, longitude)]['data'][0]['coordinates'][0]['dates']
        return measurements
    except:
        return []

if __name__ == '__main__':
    app.run('0.0.0.0', '8308')