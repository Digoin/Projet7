"""
This file is meant to test the parser as in TDD methodology
"""

from app import utils as script
from app.stopwords import a as filter

# - Parser:
#   - the stopwords filter the entry
def test_stopwords_filter():
    assert script.stopwords_filter("A la rue Martin du Gard et plus vite que ça") == ("rue Martin Gard vite")