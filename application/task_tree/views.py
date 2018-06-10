from flask import render_template, request, url_for, redirect

from application.task_tree import tree_blueprint
from application.task_tree.forms import TreeTaskForm


@tree_blueprint.route('/', methods=['GET', 'POST'])
def tree_menu():
    if request.method == 'GET':
        form = TreeTaskForm(request.values)
        return render_template('v2/task_tree/tree_menu.html', form=form)
    else:
        form = TreeTaskForm(request.form)
        if form.data['yes']:
            return redirect(url_for('root.tasks',
                                    participant=form.data['participant'],
                                    task_1_complete=form.data['task_1_complete'],
                                    task_2_complete=form.data['task_2_complete'],
                                    task_3_complete=True,
                                    task_4_complete=form.data['task_4_complete']))
        else:
            return redirect(url_for('root.tasks',
                                    participant=form.data['participant'],
                                    task_1_complete=form.data['task_1_complete'],
                                    task_2_complete=form.data['task_2_complete'],
                                    task_3_complete=form.data['task_3_complete'],
                                    task_4_complete=form.data['task_4_complete']
                                    ))
