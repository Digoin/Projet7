from password import GOOGLE_API_KEY
from .stopwords import words as filter

import requests
import json

def punctuation_filter(entry):
    punctuation = "\"._!,;:/?()\'{#-_+="

    for character in punctuation:
	    entry = entry.replace(character, "")

    return entry


def stopwords_filter(entry):
    request = entry.lower().split()
    request = request

    for noise in filter:
        if noise in request:
            request = [x for x in request if x != noise]

    return ("+".join(request))

class Geoencoder:

    def __init__(self, search):
        self.search = search
    
    def get_response(self):
        response = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}".format(self.search, GOOGLE_API_KEY))
        json_dict = response.text
        self.research(json_dict)

    def research(self, json_dict):
        results = json.loads(json_dict)["results"][0]
        latitude = results["geometry"]["location"]["lat"]
        longitude = results["geometry"]["location"]["lng"]
        address = results["formatted_address"]
        print("latitude = {}, longitude = {}, address = {}".format(latitude, longitude, address))


test = Geoencoder("5+avenue+anatole+france")
test.get_response()
