from flask_wtf import FlaskForm
from wtforms import RadioField, HiddenField, SubmitField

from application.config import Config


class ScannerTaskForm(FlaskForm):
    yes = SubmitField(label='yes')
    no = SubmitField(label='no')
    participant = HiddenField('participant')
    task_1_complete = HiddenField('task_1_complete')
    task_2_complete = HiddenField('task_2_complete')
    task_3_complete = HiddenField('task_3_complete')
    task_4_complete = HiddenField('task_4_complete')

