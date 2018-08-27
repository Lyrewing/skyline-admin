import json
import requests

HOST = "http://freecityid.market.alicloudapi.com"
PATH = "/whapi/json/alicityweather/briefforecast3days"
APPCODE = "70c6bc2c90ae456c8d82291b518376b8"

headers = {"Authorization": 'APPCODE ' + APPCODE,
           "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}


def get_weather(city_id, token):
    body = {
        "cityId": city_id,
        "token": token
    }
    url = HOST + PATH
    r = requests.post(url, data=body, headers=headers)
    response = r.content.decode(encoding="UTF-8")
    print(response)
    print(json.loads(response))


def get_city():
    pass


get_weather(2, "677282c2f1b3d718152c4e25ed434bc4")
