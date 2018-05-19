from flask import render_template, request, url_for, redirect

from application.task_swipe import swipe_blueprint
from application.task_swipe.forms import SwipeMenuForm, ConfirmForm, EndTaskForm


@swipe_blueprint.route('/', methods=['GET', 'POST'])
def swipe_menu():
    if request.method == 'GET':
        form = SwipeMenuForm(request.values)
        return render_template('v2/task_swipe/swipe_menu.html', form=form)
    else:
        form = SwipeMenuForm(request.form)
        if form.data['yes']:
            return redirect(url_for('swipe.confirm',
                                    participant=form.data['participant'],
                                    task_1_complete=form.data['task_1_complete'],
                                    task_2_complete=form.data['task_2_complete'],
                                    task_3_complete=form.data['task_3_complete'],
                                    choice=form.data['icons']))
        else:
            return redirect(url_for('root.tasks',
                                    participant=form.data['participant'],
                                    task_1_complete=form.data['task_1_complete'],
                                    task_2_complete=form.data['task_2_complete'],
                                    task_3_complete=form.data['task_3_complete']))


@swipe_blueprint.route('/confirm', methods=['GET', 'POST'])
def confirm():
    if request.method == 'GET':
        form = ConfirmForm(request.values)
        return render_template('v2/task_swipe/confirm.html', form=form, item_choice=request.args['choice'])
    else:
        form = ConfirmForm(request.form)
        if form.data['yes']:
            return redirect(url_for('swipe.end_task',
                                    participant=form.data['participant'],
                                    task_1_complete=form.data['task_1_complete'],
                                    task_2_complete=form.data['task_2_complete'],
                                    task_3_complete=form.data['task_3_complete'],
                                    choice=form.data['choice']))
        else:
            return redirect(url_for('swipe.swipe_menu',
                                    participant=form.data['participant'],
                                    task_1_complete=form.data['task_1_complete'],
                                    task_2_complete=form.data['task_2_complete'],
                                    task_3_complete=form.data['task_3_complete']))


@swipe_blueprint.route('/end-task', methods=['GET', 'POST'])
def end_task():
    if request.method == 'GET':
        form = EndTaskForm(request.values)
        return render_template('v2/task_swipe/end_task.html', form=form, item_choice=request.args['choice'])
    else:
        form = EndTaskForm(request.form)
        return redirect(url_for('root.tasks',
                                participant=form.data['participant'],
                                task_1_complete=form.data['task_1_complete'],
                                task_2_complete=True,
                                task_3_complete=form.data['task_3_complete']))