import json
import requests

HOST = "http://freecityid.market.alicloudapi.com"
PATH = "/whapi/json/alicityweather/briefforecast3days"
APPCODE = "70c6bc2c90ae456c8d82291b518376b8"


def get_weather(cityId, token):
    body = {
        "cityId": cityId,
        "token": token
    }
    url = HOST + PATH
    headers = {"Authorization": 'APPCODE ' + APPCODE,
               "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
    r = requests.post(url, data=body, headers=headers)
    response = r.content.decode(encoding="UTF-8")
    print(response)
    print(json.loads(response))


get_weather(2, "677282c2f1b3d718152c4e25ed434bc4")
