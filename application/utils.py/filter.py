from .stopwords import words as filter

class Filter:

    def punctuation(self, entry):
        punctuation = "\"._!,;:/?()\'{#-_+="

        for character in punctuation:
            entry = entry.replace(character, "")

        return entry


    def stopwords(self, entry):
        request = entry.lower().split()
        request = request

        for noise in filter:
            if noise in request:
                request = [x for x in request if x != noise]

        return ("+".join(request))
