from flask_wtf import FlaskForm
from wtforms import RadioField, HiddenField, SubmitField
from wtforms.validators import DataRequired


class ParticipantForm(FlaskForm):
    participant = RadioField('Participant', choices=[(d, 'Participant %d' % d) for d in range(1, 21)], validators=[DataRequired()])
    start = SubmitField(label='start')


class TaskListForm(FlaskForm):
    yes = SubmitField(label='yes')
    no = SubmitField(label='no')

    participant = HiddenField('participant')
    task_1_complete = HiddenField('task_1_complete')
    task_2_complete = HiddenField('task_2_complete')
    task_3_complete = HiddenField('task_3_complete')
    task_4_complete = HiddenField('task_4_complete')

    choices = [('task_1', 'Icon Menu'), ('task_2', 'Swipe Menu'),
               ('task_3', 'Original Menu'), ('task_4', 'Alternate Device')]
    task = RadioField('Task', choices=choices)


class TaskForm(FlaskForm):
    participant = HiddenField('participant')
    task_1_complete = HiddenField('task_1_complete')
    task_2_complete = HiddenField('task_2_complete')
    task_3_complete = HiddenField('task_3_complete')
    task_4_complete = HiddenField('task_4_complete')
