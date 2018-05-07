from flask import render_template

from application.home import home_blueprint
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class HomeForm(FlaskForm):

    participant = StringField(label='Participant', validators=[DataRequired()])


@home_blueprint.route('/')
def index():
    form = HomeForm()
    return render_template('home.html', form=form)
