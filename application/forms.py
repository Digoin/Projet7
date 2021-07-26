from wtforms import Form, StringField, validators

class QuestionForm(Form):
    question = StringField("Question", [validators.Length(max=100)])
