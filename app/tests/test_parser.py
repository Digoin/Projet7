"""
This file is meant to test the parser as in TDD methodology
"""

from app import utils as script
# - Parser:
#   - filter the punctuation
def test_punctuation_filter():
    assert script.punctuation_filter("A la rue \"(Roger) Martin du Gard\", et plus vite que ça!!!") == "A la rue Roger Martin du Gard et plus vite que ça"
#   - the stopwords filter the entry
def test_stopwords_filter():
    assert script.stopwords_filter("A la rue Roger Martin du Gard et plus vite que ça") == "rue+roger+martin+gard+vite"

