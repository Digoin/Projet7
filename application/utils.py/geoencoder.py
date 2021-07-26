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
