import requests
import json


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
