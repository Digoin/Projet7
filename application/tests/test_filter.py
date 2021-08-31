"""
This file is meant to test the filter as in TDD methodology
"""

from application.utils.filter import Filter

# - Filter:
filter = Filter()

#   - filter the punctuation
def test_punctuation():
    assert (
        filter.punctuation('A la rue "(Roger) Martin du Gard", et plus vite que ça!!!')
        == "A la rue Roger Martin du Gard et plus vite que ça"
    )


#   - the stopwords filter the entry
def test_stopwords():
    assert (
        filter.stopwords("A la rue Roger Martin du Gard et plus vite que ça")
        == "rue+roger+martin+gard+vite"
    )


def test_abbreviation():
    assert filter.abbreviation("5 Av. Anatole France") == "5 Avenue Anatole France"
