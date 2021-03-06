"""
This file is meant to test the geoencoder class as in TDD methodology
"""

from application.utils.geoencoder import Geoencoder
import json


# - Geoencoder:
geo = Geoencoder()

#   - find the location and address
def test_parse_address():
    with open("application/tests/mocks/address_dict.json") as file:
        JSON_DICT = json.load(file)

    test_dict = {
        "latitude": 44.8496861,
        "longitude": -0.5085099,
        "address": "1 Rue Martin du Gard, 33150 Cenon, France",
    }

    geo_search = geo.parse_address(JSON_DICT)

    assert geo_search["latitude"] == test_dict["latitude"]
    assert geo_search["longitude"] == test_dict["longitude"]
    assert geo_search["address"] == test_dict["address"]
