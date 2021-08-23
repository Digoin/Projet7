from wtforms import Form, StringField, validators


class QuestionForm(Form):
    """This class is meant to help the creation of forms in the project"""

    question = StringField("Question", [validators.Length(max=100)])
