"""This file call the wikipedia API and return some information"""

import json
import requests


class Wikipedia:
    def research_address(self, location):
        """This function call the wikipedia API with the reponse of the google maps API"""
        address = location["address"]
        research = address.replace(" ", "+")
        response = requests.get(
            f"https://fr.wikipedia.org/w/api.php?action=query&list=search&srsearch={research}&format=json"
        )
        return response.text

    def research_address_title(self, json_dict):
        """This function get the title of the wikipedia response"""
        try:
            title = json.loads(json_dict)["query"]["search"][0]["title"]
        except IndexError:
            return None
        return title

    def research_place(self, title):
        """This funciton call the wikipedia API with the title we got before"""
        research = title.replace(" ", "+")
        response = requests.get(
            f"https://fr.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&titles={research}&formatversion=2&exsentences=5&exlimit=1&explaintext=1"
        )
        return response.text

    def research_place_extract(self, json_dict):
        """This function get the desription of the search"""
        extract = json.loads(json_dict)["query"]["pages"][0]["extract"]
        return extract

    def correction(self, extract):
        "This funtion delete the line breaks of the response"
        corrected = extract.replace("\n", "")
        return corrected
