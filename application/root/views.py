from flask import render_template, request, url_for, redirect

from application.root import root_blueprint
from application.root.forms import ParticipantForm, TaskForm


@root_blueprint.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        form = ParticipantForm()
        return render_template('v2/start.html', form=form)
    else:
        form = ParticipantForm(request.form)
        return redirect(url_for('root.tasks',
                                participant=form.data['participant'],
                                task_1_complete=False, task_2_complete=False, task_3_complete=False))


@root_blueprint.route('/tasks', methods=['GET', 'POST'])
def tasks():
    if request.method == 'GET':
        form = TaskForm(request.values)
        return render_template('v2/tasks.html', form=form)
    else:
        form = TaskForm(request.form)
        if form.data['task'] == 'task_1':
            return redirect(url_for('icons.icon_menu',
                                    participant=form.data['participant'],
                                    task_1_complete=form.data['task_1_complete'],
                                    task_2_complete=form.data['task_2_complete'],
                                    task_3_complete=form.data['task_3_complete']))
        elif form.data['task'] == 'task_2':
            return redirect(url_for('swipe.swipe_menu',
                                    participant=form.data['participant'],
                                    task_1_complete=form.data['task_1_complete'],
                                    task_2_complete=form.data['task_2_complete'],
                                    task_3_complete=form.data['task_3_complete']))
        elif form.data['task'] == 'Original Menu':
            pass
