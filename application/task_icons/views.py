from flask import render_template, request, url_for, redirect

from application.task_icons import icons_blueprint
from application.task_icons.forms import IconMenuForm, ConfirmForm, EndTaskForm

images = {
    'Antelope':'images/animals/antelope.png',
    'Bear':'images/animals/bear.png',
    'Bee':'images/animals/bee.png',
    'Camel':'images/animals/camel.png',
    'Dog':'images/animals/dog.png',
    'Dolphin':'images/animals/dolphin.png',
    'Dragonfly':'images/animals/dragonfly.png',
    'Duck':'images/animals/duck.png',
    'Elephant':'images/animals/elephant.png',
    'Fish':'images/animals/fish.png',
    'Fox':'images/animals/fox.png',
    'Frog':'images/animals/frog.png',
    'Gnat':'images/animals/gnat.png',
    'Hawk':'images/animals/hawk.png',
    'Horse':'images/animals/horse.png',
    'Koala':'images/animals/koala.png',
    'Pig':'images/animals/pig.png',
    'Pigeon':'images/animals/pigeon.png',
    'Sheep':'images/animals/sheep.png',
    'Stag':'images/animals/stag.png',
    'Swan':'images/animals/swan.png',
    'Trout':'images/animals/trout.png',
    'Walrus':'images/animals/walrus.png',
    'Wasp':'images/animals/wasp.png',
    'Zebra':'images/animals/zebra.png'
}

@icons_blueprint.route('/', methods=['GET', 'POST'])
def icon_menu():
    if request.method == 'GET':
        form = IconMenuForm(request.values)
        return render_template('v2/task_icons/icon_menu.html', form=form, rows=6, cols=4)
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