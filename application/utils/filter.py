"""This file is used to transform some strings"""

from .stopwords import words


class Filter:
    def punctuation(self, entry):
        """This function delete the punctuation from the string"""
        punctuation = "\"._!,;:/?()'{#-_="

        for character in punctuation:
            entry = entry.replace(character, "")

        return entry

    def stopwords(self, entry):
        """This function delete the generics words from the string"""
        request = entry.lower().split()

        for noise in words:
            if noise in request:
                request = [x for x in request if x != noise]

        return "+".join(request)

    def abbreviation(self, entry):
        """This function transform Av. to Avenue"""
        return entry.replace("Av.", "Avenue")
