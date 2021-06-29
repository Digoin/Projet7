from stopwords import words as filter

def stopwords_filter(entry):
    request = entry.split()

    for noise in filter:
        if noise in request:
            request = [x for x in request if x != noise]

    print (" ".join(request))

stopwords_filter("A la rue Martin du Gard et plus vite que ça")