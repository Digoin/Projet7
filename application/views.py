import json
from flask import Flask, render_template, request
from werkzeug.utils import redirect
from werkzeug.wrappers import response
from flask_cors import CORS
from .utils import Filter, Geoencoder, Wikipedia
# from .test import parser
from .forms import QuestionForm
from . import utils


app = Flask(__name__)

CORS(app)

app.config.from_object('config')


@app.route("/")
def base():
    return render_template("question.html")

@app.route('/question/<form_data>')
def question(form_data):
    data_filter = Filter()
    geoencoder = Geoencoder()
    wikipedia = Wikipedia()

    punctuation_filtered = data_filter.punctuation(form_data["question"])
    filtered = data_filter.stopwords(punctuation_filtered)

    geo_response = geoencoder.get_response(filtered)
    location = geoencoder.parse_address(geo_response)

    address_dict = wikipedia.research_address(location)
    title = wikipedia.research_address_title(address_dict)
    if title == None:
        address = location["address"]
        return f"Je n'ai pas d'anecdote sur \"{address}\" à te raconter mon enfant."
    place_dict = wikipedia.research_place(title)
    extract = wikipedia.research_place_extract(place_dict)
    data = wikipedia.correction(extract)

    return data

@app.route("/api/")
def api():
    return json.dumps({
        "status": "ok",
        "response": 7
    })

@app.route("/index/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
