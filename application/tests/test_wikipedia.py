"""
This file is meant to test the wikipedia reseazrch as in TDD methodology
"""

from app import utils as script

# https://fr.wikipedia.org/w/api.php?action=query&list=search&srsearch=Tour+Eiffel&format=json
# https://fr.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&titles=Tour+Eiffel&formatversion=2&exsentences=5&exlimit=1&explaintext=1

# - Wikipedia:
#   - The specific research use the global article research first response as titles
#   - The "\n" are erased
# def test_correction():
#     sentence = "La tour Eiffel est une tour de fer puddlé de 324 mètres de hauteur (avec antennes) située à Paris."
#     assert script.correction("\nLa tour Eiffel\n est une tour de fer puddlé \nde 324 mètres\n de haut\neur (avec antennes) située à Paris.\n") == sentence
