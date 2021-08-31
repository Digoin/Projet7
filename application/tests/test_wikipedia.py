"""
This file is meant to test the wikipedia research as in TDD methodology
"""

from application.utils.wikipedia import Wikipedia
import json

# - Wikipedia:
wiki = Wikipedia()

#   - find the title of the research
def test_research_address_title():
    with open("application/tests/mocks/research_title.json") as file:
        assert wiki.research_address_title(file.read()) == "Tour Eiffel"

#   - find the extract of the research
def test_research_place_extract():
    with open("application/tests/mocks/research_extract.json") as file:
        assert wiki.research_place_extract(file.read()) ==  "La Tour Eiffel est dans Paris"

#   - The "\n" are erased
def test_correction():
    sentence = "La tour Eiffel est une tour de fer puddlé de 324 mètres de hauteur (avec antennes) située à Paris."
    assert wiki.correction("\nLa tour Eiffel\n est une tour de fer puddlé \nde 324 mètres\n de haut\neur (avec antennes) située à Paris.\n") == sentence
