from flask import render_template, request, url_for, redirect

from application.config import Config
from application.root import root_blueprint
from application.root.forms import ParticipantForm, TaskListForm, TaskForm


@root_blueprint.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        form = ParticipantForm()
        return render_template('index.html', form=form)
    else:
        form = ParticipantForm(request.form)
        print('Participant', form.data['participant'])
        if form.data['participant'] == 'None':
            return redirect(url_for('root.index'))

        return redirect(url_for('root.tasks',
                                participant=form.data['participant'],
                                task_1_complete=False, task_2_complete=False, task_3_complete=False,
                                task_4_complete=False))


@root_blueprint.route('/tasks', methods=['GET', 'POST'])
def tasks():
    if request.method == 'GET':
        form = TaskListForm(request.values)

        return render_template('tasks.html', form=form,
                               task_order=order_for_participant(request.values['participant']))
    else:
        form = TaskListForm(request.form)
        if form.data['yes']:
            if form.data['task'] == 'task_1':
                return redirect(url_for('root.icon_menu',
                                        participant=form.data['participant'],
                                        task_1_complete=form.data['task_1_complete'],
                                        task_2_complete=form.data['task_2_complete'],
                                        task_3_complete=form.data['task_3_complete'],
                                        task_4_complete=form.data['task_4_complete']))
            elif form.data['task'] == 'task_2':
                return redirect(url_for('swipe.swipe_menu',
                                        participant=form.data['participant'],
                                        task_1_complete=form.data['task_1_complete'],
                                        task_2_complete=form.data['task_2_complete'],
                                        task_3_complete=form.data['task_3_complete'],
                                        task_4_complete=form.data['task_4_complete']))
            elif form.data['task'] == 'task_3':
                return redirect(url_for('tree.tree_menu',
                                        participant=form.data['participant'],
                                        task_1_complete=form.data['task_1_complete'],
                                        task_2_complete=form.data['task_2_complete'],
                                        task_3_complete=form.data['task_3_complete'],
                                        task_4_complete=form.data['task_4_complete']))
            elif form.data['task'] == 'task_4':
                return redirect(url_for('scanner.scanner_menu',
                                        participant=form.data['participant'],
                                        task_1_complete=form.data['task_1_complete'],
                                        task_2_complete=form.data['task_2_complete'],
                                        task_3_complete=form.data['task_3_complete'],
                                        task_4_complete=form.data['task_4_complete']))
            else:
                return redirect(url_for('root.index'))
        else:
            return redirect(url_for('root.index'))


def order_for_participant(participant):
    return [(int(participant) + i - 1) % 4 for i in range(0, 4)]


@root_blueprint.route('/icon-menu')
def icon_menu():
    form = TaskForm(request.values)
    return render_template('tasks/icon_menu.html', form=form, rows=5, cols=4, icons=Config.CHOICES)


@root_blueprint.route('/swipe-cards')
def swipe_cards():
    form = TaskForm(request.values)
    return render_template('tasks/swipe_cards.html', form=form, cards=Config.CHOICES)


@root_blueprint.route('/sub-menus')
def sub_menus():
    form = TaskForm(request.values)
    return render_template('tasks/sub_menu.html', form=form, cards=Config.CHOICES)


@root_blueprint.route('/external')
def external():
    form = TaskForm(request.values)
    return render_template('tasks/external.html', form=form)