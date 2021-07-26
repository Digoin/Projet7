import json
from flask import Flask, render_template, request
from werkzeug.utils import redirect
from werkzeug.wrappers import response
from flask_cors import CORS

from .forms import QuestionForm
from . import utils


app = Flask(__name__)

CORS(app)

app.config.from_object('config')

@app.route('/', methods=["GET", "POST"])
def question():
    form = QuestionForm(request.form)
    if request.method == "POST" and form.validate():
        form_data = form.data
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
            return render_template("answer.html", description=f"Je n'ai pas d'anecdote sur \"{address}\" à te raconter mon enfant.")
        place_dict = wikipedia.research_place(title)
        extract = wikipedia.research_place_extract(place_dict)
        data = wikipedia.correction(extract)

        return render_template("answer.html", description=data)
    return render_template("question.html", form=form)

@app.route("/answer/")
def answer():
    return render_template("answer.html")

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
