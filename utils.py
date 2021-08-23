from .stopwords import words as filter

class Filter:

    def punctuation(self, entry):
        punctuation = "\"._!,;:/?()\'{#-_+="

        for character in punctuation:
            entry = entry.replace(character, "")

        return entry


    def stopwords(self, entry):
        request = entry.lower().split()
        request = request

        for noise in filter:
            if noise in request:
                request = [x for x in request if x != noise]

        return ("+".join(request))


from password import GOOGLE_API_KEY

import requests
import json

class Geoencoder:
    
    def get_response(self, search):
        response = requests.get(f"https://maps.googleapis.com/maps/api/geocode/json?address={search}&key={GOOGLE_API_KEY}")
        return json.loads(response.text)

    def parse_address(self, data):
        results = data["results"][0]
        latitude = results["geometry"]["location"]["lat"]
        longitude = results["geometry"]["location"]["lng"]
        address = results["formatted_address"]
        return {
            "latitude" : latitude,
            "longitude" : longitude,
            "address" : address
        }


class Wikipedia:

    def research_address(self, location):
        address = location["address"]
        research = address.replace(" ", "+")
        response = requests.get("https://fr.wikipedia.org/w/api.php?action=query&list=search&srsearch={}&format=json".format(research))
        address_dict = response.text
        return address_dict
    
    def research_address_title(self, json_dict):
        print(json_dict)
        try:
            title = json.loads(json_dict)["query"]["search"][0]["title"]
        except IndexError:
            return None
        return title
    
    def research_place(self, title):
        research = title.replace(" ", "+")
        response = requests.get("https://fr.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&titles={}&formatversion=2&exsentences=5&exlimit=1&explaintext=1".format(research))
        location_dict = response.text
        return location_dict
    
    def research_place_extract(self, json_dict):
        extract = json.loads(json_dict)["query"]["pages"][0]["extract"]
        return extract

    def correction(self, extract):
        corrected = extract.replace("\n", "")
        return corrected
