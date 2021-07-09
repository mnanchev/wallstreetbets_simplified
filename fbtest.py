
import requests
import json


def writeToFireBase():
    url = 'https://wsbsimplified-default-rtdb.firebaseio.com/'
    body = {'name': 'Maryja'}
    headers = {'content-type': 'application/json'}

    r = requests.post(url, data=json.dumps(body), headers=headers)