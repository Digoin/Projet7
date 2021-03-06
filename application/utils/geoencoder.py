"""This file call the google maps API and return some information"""

import json
import requests
import os


class Geoencoder:
    def get_response(self, search):
        """This function call the google maps API with the question of the user"""
        response = requests.get(
            f"https://maps.googleapis.com/maps/api/geocode/json?address={search}&key={os.getenv('GOOGLE_API_KEY')}"
        )
        return json.loads(response.text)

    def parse_address(self, data):
        "This function search for the desired content of the API response"
        try:
            results = data["results"][0]
        except IndexError:
            return None
        latitude = results["geometry"]["location"]["lat"]
        longitude = results["geometry"]["location"]["lng"]
        address = results["formatted_address"]
        return {"latitude": latitude, "longitude": longitude, "address": address}
