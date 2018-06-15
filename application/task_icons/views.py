from flask import render_template, request, url_for, redirect

from application.config import Config
from application.task_icons import icons_blueprint
from application.task_icons.forms import IconMenuForm, ConfirmForm, EndTaskForm


@icons_blueprint.route('/', methods=['GET', 'POST'])
def icon_menu():
    images = {choice['item']: 'images/icons/%s' % choice['image'] for choice in Config.CHOICES}

    if request.method == 'GET':
        form = IconMenuForm(request.values)
        return render_template('v2/task_icons/icon_menu.html', form=form, rows=5, cols=4, icons=Config.CHOICES)
    else:
        form = IconMenuForm(request.form)
        if form.data['yes']:
            return redirect(url_for('icons.confirm',
                                    participant=form.data['participant'],
                                    task_1_complete=form.data['task_1_complete'],
                                    task_2_complete=form.data['task_2_complete'],
                                    task_3_complete=form.data['task_3_complete'],
                                    task_4_complete=form.data['task_4_complete'],
                                    choice=form.data['icons'],
                                    images=images))
        else:
            return redirect(url_for('root.tasks',
                                    participant=form.data['participant'],
                                    task_1_complete=form.data['task_1_complete'],
                                    task_2_complete=form.data['task_2_complete'],
                                    task_3_complete=form.data['task_3_complete'],
                                    task_4_complete=form.data['task_4_complete']
                                    ))


@icons_blueprint.route('/confirm', methods=['GET', 'POST'])
def confirm():
    if request.method == 'GET':
        form = ConfirmForm(request.values)
        return render_template('v2/task_icons/confirm.html', form=form, item_choice=request.args['choice'])
    else:
        form = ConfirmForm(request.form)
        if form.data['yes']:
            return redirect(url_for('icons.end_task',
                                    participant=form.data['participant'],
                                    task_1_complete=form.data['task_1_complete'],
                                    task_2_complete=form.data['task_2_complete'],
                                    task_3_complete=form.data['task_3_complete'],
                                    task_4_complete=form.data['task_4_complete'],
                                    choice=form.data['choice']))
        else:
            return redirect(url_for('icons.icon_menu',
                                    participant=form.data['participant'],
                                    task_1_complete=form.data['task_1_complete'],
                                    task_2_complete=form.data['task_2_complete'],
                                    task_3_complete=form.data['task_3_complete'],
                                    task_4_complete=form.data['task_4_complete']
                                    ))


@icons_blueprint.route('/end-task', methods=['GET', 'POST'])
def end_task():
    if request.method == 'GET':
        form = EndTaskForm(request.values)
        return render_template('v2/task_icons/end_task.html', form=form, item_choice=request.args['choice'])
    else:
        form = EndTaskForm(request.form)
        return redirect(url_for('root.tasks',
                                participant=form.data['participant'],
                                task_1_complete=True,
                                task_2_complete=form.data['task_2_complete'],
                                task_3_complete=form.data['task_3_complete'],
                                task_4_complete=form.data['task_4_complete']
                                ))
