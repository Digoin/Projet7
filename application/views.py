"""This file contain all the website url and python functions calls"""
import json
from flask import Flask, render_template
from flask_cors import CORS
from .utils.filter import Filter
from .utils.geoencoder import Geoencoder
from .utils.wikipedia import Wikipedia


app = Flask(__name__)

CORS(app)

app.config.from_object("config")


"""This is the main webpage"""


@app.route("/")
def base():
    return render_template("question.html")


"""This is called when the user validate the form"""


@app.route("/question/<form_data>")
def question(form_data):
    data_filter = Filter()
    geoencoder = Geoencoder()
    wikipedia = Wikipedia()

    # we pass the request through filters so maps can understand the request
    punctuation_filtered = data_filter.punctuation(form_data)
    filtered = data_filter.stopwords(punctuation_filtered)

    # we ask the request to the google maps API
    geo_response = geoencoder.get_response(filtered)
    location = geoencoder.parse_address(geo_response)

    # we use the google maps API repsponse and use it on wikipedia API
    location["address"] = data_filter.abbreviation(location["address"])
    address_dict = wikipedia.research_address(location)
    title = wikipedia.research_address_title(address_dict)

    # if wikipedia dont find anything about the address, GrandpyBOT will say it
    if title is None:
        address = location["address"]
        response = json.dumps(
            {
                "response": f"Je n'ai pas d'anecdote sur \"{address}\" à te raconter mon enfant.",
                "status": "empty",
                "latitude": location["latitude"],
                "longitude": location["longitude"],
            }
        )
        return response

    # we set some variable so js can use it
    place_dict = wikipedia.research_place(title)
    extract = wikipedia.research_place_extract(place_dict)
    data = wikipedia.correction(extract)
    response = json.dumps(
        {
            "response": data,
            "status": "ok",
            "latitude": location["latitude"],
            "longitude": location["longitude"],
        }
    )

    return response


if __name__ == "__main__":
    app.run()
