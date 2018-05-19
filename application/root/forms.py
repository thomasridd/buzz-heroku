from flask_wtf import FlaskForm
from wtforms import RadioField, HiddenField


class ParticipantForm(FlaskForm):
    participant = RadioField('Participant', choices=[('orange', 'Orange participant'),
                                                     ('red', 'Red participant'),
                                                     ('white', 'White participant'),
                                                     ('green', 'Green participant'),
                                                     ('blue', 'Blue participant'),
                                                     ('purple', 'Purple participant'),
                                                     ('yellow', 'Yellow participant'),
                                                     ('black', 'Black participant')])


class TaskForm(FlaskForm):
    task = RadioField('Task', choices=[('task_1', 'Icon Menu'), ('task_2', 'Swipe Menu'), ('task_3', 'Original Menu')])

    participant = HiddenField('participant')
    task_1_complete = HiddenField('task_1_complete')
    task_2_complete = HiddenField('task_2_complete')
    task_3_complete = HiddenField('task_3_complete')

