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
        self.json_dict = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}".format(search, GOOGLE_API_KEY))
    
    def research(self):
        location = json.loads(self.json_dict.text)["results"][0]["geometry"]["location"]
        latitude = location["lat"]
        longitude = location["lng"]
        print("latitude = {}, longitude = {}".format(latitude, longitude))


test = Geoencoder("rue+martin+du+gard")
test.research()
