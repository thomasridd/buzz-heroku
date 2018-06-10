from flask_wtf import FlaskForm
from wtforms import HiddenField, SubmitField


class TreeTaskForm(FlaskForm):
    yes = SubmitField(label='yes')
    no = SubmitField(label='no')
    participant = HiddenField('participant')
    task_1_complete = HiddenField('task_1_complete')
    task_2_complete = HiddenField('task_2_complete')
    task_3_complete = HiddenField('task_3_complete')
    task_4_complete = HiddenField('task_4_complete')
