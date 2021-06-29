"""
This file is meant to test the parser as in TDD methodology
"""

import parser as script

# - Parser:
#   - the stopwords filter the entry
    def test_stopwords_filter():
        entry = script.stopwords_filter("A la rue Martin du Gard et plus vite que ça")
        assert entry == ("rue Martin Gard vite")