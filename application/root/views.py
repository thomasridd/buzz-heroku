from flask import render_template, request, url_for, redirect

from application.config import Config
from application.root import root_blueprint
from application.root.forms import ParticipantForm, TaskListForm, TaskForm, EndTaskForm


@root_blueprint.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        form = ParticipantForm()
        return render_template('index.html', form=form)
    else:
        form = ParticipantForm(request.form)
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
                return redirect(url_for('root.swipe_cards',
                                        participant=form.data['participant'],
                                        task_1_complete=form.data['task_1_complete'],
                                        task_2_complete=form.data['task_2_complete'],
                                        task_3_complete=form.data['task_3_complete'],
                                        task_4_complete=form.data['task_4_complete']))
            elif form.data['task'] == 'task_3':
                return redirect(url_for('root.sub_menus',
                                        participant=form.data['participant'],
                                        task_1_complete=form.data['task_1_complete'],
                                        task_2_complete=form.data['task_2_complete'],
                                        task_3_complete=form.data['task_3_complete'],
                                        task_4_complete=form.data['task_4_complete']))
            elif form.data['task'] == 'task_4':
                return redirect(url_for('root.external',
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


@root_blueprint.route('/icon-menu', methods=['GET', 'POST'])
def icon_menu():

    if request.method == 'GET':
        form = TaskForm(request.values)
        return render_template('tasks/icon_menu.html', form=form, rows=5, cols=4, icons=Config.CHOICES)
    else:
        form = EndTaskForm(request.values)

        task_1_complete = True if form.data['yes'] else form.data['task_1_complete']
        return redirect(url_for('root.tasks',
                                participant=form.data['participant'],
                                task_1_complete=task_1_complete,
                                task_2_complete=form.data['task_2_complete'],
                                task_3_complete=form.data['task_3_complete'],
                                task_4_complete=form.data['task_4_complete']))


@root_blueprint.route('/swipe-cards', methods=['GET', 'POST'])
def swipe_cards():

    if request.method == 'GET':
        form = TaskForm(request.values)
        return render_template('tasks/swipe_cards.html', form=form, cards=Config.CHOICES)
    else:
        form = EndTaskForm(request.values)

        task_2_complete = True if form.data['yes'] else form.data['task_2_complete']
        return redirect(url_for('root.tasks',
                                participant=form.data['participant'],
                                task_1_complete=form.data['task_1_complete'],
                                task_2_complete=task_2_complete,
                                task_3_complete=form.data['task_3_complete'],
                                task_4_complete=form.data['task_4_complete']))


@root_blueprint.route('/sub-menus', methods=['GET', 'POST'])
def sub_menus():
    if request.method == 'GET':
        form = TaskForm(request.values)
        return render_template('tasks/sub_menu.html', form=form, tree=Config.TREE)
    else:
        form = EndTaskForm(request.values)

        task_3_complete = True if form.data['yes'] else form.data['task_3_complete']
        return redirect(url_for('root.tasks',
                                participant=form.data['participant'],
                                task_1_complete=form.data['task_1_complete'],
                                task_2_complete=form.data['task_2_complete'],
                                task_3_complete=task_3_complete,
                                task_4_complete=form.data['task_4_complete']))


@root_blueprint.route('/external', methods=['GET', 'POST'])
def external():

    if request.method == 'GET':
        form = TaskForm(request.values)
        return render_template('tasks/external.html', form=form)
    else:
        form = EndTaskForm(request.values)

        task_4_complete = True if form.data['yes'] else form.data['task_4_complete']
        return redirect(url_for('root.tasks',
                            participant=form.data['participant'],
                            task_1_complete=form.data['task_1_complete'],
                            task_2_complete=form.data['task_2_complete'],
                            task_3_complete=form.data['task_3_complete'],
                            task_4_complete=task_4_complete))
