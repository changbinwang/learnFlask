from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

__author__ = 'owen2785'


class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')