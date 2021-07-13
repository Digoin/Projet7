"""
This file is meant to test the geoencoder class as in TDD methodology
"""

from app import utils as script
import json


# - Geoencoder:
# class TestGeoencoder:
#     JSON_DICT = {
#         "results" : [
#             {
#                 "formatted_address" : "1 Rue Martin du Gard, 33150 Cenon, France",
#                 "geometry" : {
#                     "location" : {
#                     "lat" : 44.8496861,
#                     "lng" : -0.5085099
#                     }
#                 }
#             }
#         ]
#     }
#   - find the location and address
    # def test_research(self, monkeypatch):
    #     monkeypatch.delattr(json.loads, "self.JSON_DICT")

    #     geoencoder = script.Geoencoder(None)
    #     assert geoencoder.research(self.JSON_DICT) == "latitude = 44.8496861, longitude = -0.5085099, address = 1 Rue Martin du Gard, 33150 Cenon, France"
