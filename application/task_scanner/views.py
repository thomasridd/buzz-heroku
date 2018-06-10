from flask import render_template, request, url_for, redirect

from application.task_scanner import scanner_blueprint
from application.task_scanner.forms import ScannerTaskForm


@scanner_blueprint.route('/', methods=['GET', 'POST'])
def scanner_menu():
    if request.method == 'GET':
        form = ScannerTaskForm(request.values)
        return render_template('v2/task_scanner/scanner_menu.html', form=form)
    else:
        form = ScannerTaskForm(request.form)
        if form.data['yes']:
            return redirect(url_for('root.tasks',
                                    participant=form.data['participant'],
                                    task_1_complete=form.data['task_1_complete'],
                                    task_2_complete=form.data['task_2_complete'],
                                    task_3_complete=form.data['task_3_complete'],
                                    task_4_complete=True))
        else:
            return redirect(url_for('root.tasks',
                                    participant=form.data['participant'],
                                    task_1_complete=form.data['task_1_complete'],
                                    task_2_complete=form.data['task_2_complete'],
                                    task_3_complete=form.data['task_3_complete'],
                                    task_4_complete=form.data['task_4_complete']))
