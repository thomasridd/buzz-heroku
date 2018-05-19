from flask_wtf import FlaskForm
from wtforms import RadioField, HiddenField, SubmitField

from application.config import Config


class TreeLevelOneForm(FlaskForm):
    yes = SubmitField(label='yes')
    no = SubmitField(label='no')
    participant = HiddenField('participant')
    task_1_complete = HiddenField('task_1_complete')
    task_2_complete = HiddenField('task_2_complete')
    task_3_complete = HiddenField('task_3_complete')

    choices = [(choice['item'], choice['value']) for choice in Config.CHOICES]
    icons = RadioField('Icons', choices=choices)


class TreeLevelTwoForm(FlaskForm):
    yes = SubmitField(label='yes')
    no = SubmitField(label='no')
    participant = HiddenField('participant')
    task_1_complete = HiddenField('task_1_complete')
    task_2_complete = HiddenField('task_2_complete')
    task_3_complete = HiddenField('task_3_complete')

    choices = [(choice['item'], choice['value']) for choice in Config.CHOICES]
    icons = RadioField('Icons', choices=choices)


class ConfirmForm(FlaskForm):
    yes = SubmitField(label='yes')
    no = SubmitField(label='no')
    participant = HiddenField('participant')
    task_1_complete = HiddenField('task_1_complete')
    task_2_complete = HiddenField('task_2_complete')
    task_3_complete = HiddenField('task_3_complete')
    choice = HiddenField('choice')


class EndTaskForm(FlaskForm):
    participant = HiddenField('participant')
    task_1_complete = HiddenField('task_1_complete')
    task_2_complete = HiddenField('task_2_complete')
    task_3_complete = HiddenField('task_3_complete')
    choice = HiddenField('choice')