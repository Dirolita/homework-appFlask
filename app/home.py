from flask import Blueprint, render_template, request, redirect, url_for
import json
import os
from datetime import datetime

bp = Blueprint('home', __name__)

@bp.route('/home', methods=['GET', 'POST'])
def home():
    username = request.args.get('username')
    tasks_file_path = f"{username}_tasks.json"

    tasks_data = []

    if request.method == 'POST':
        task = request.form.get('task')
        date = request.form.get('date')
        category = request.form.get('categoria')
        state = request.form.get('state')

        if task and date and category and state:
            if os.path.exists(tasks_file_path):
                with open(tasks_file_path, 'r') as file:
                    tasks_data = json.load(file)
            else:
                tasks_data = []

            new_task = {'task': task, 'date': date, 'category': category, 'state': state}
            tasks_data.insert(0, new_task)  # Insertar en la primera posición

            with open(tasks_file_path, 'w') as file:
                json.dump(tasks_data, file)

        return redirect(url_for('home.home', username=username))

    else:
        if os.path.exists(tasks_file_path):
            with open(tasks_file_path, 'r') as file:
                tasks_data = json.load(file)

    return render_template('home.html', username=username, tasks=tasks_data)


@bp.route('/update_task/<username>/<int:task_index>', methods=['POST'])
def update_task(username, task_index):
    tasks_file_path = f"{username}_tasks.json"

    if os.path.exists(tasks_file_path):
        with open(tasks_file_path, 'r') as file:
            tasks_data = json.load(file)
    else:
        tasks_data = []

    tasks_data[task_index]['state'] = 'Finalizado'
    tasks_data[task_index]['fecha_finalizacion'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(tasks_file_path, 'w') as file:
        json.dump(tasks_data, file)

    return redirect(url_for('home.home', username=username))

@bp.route('/delete_task/<username>/<int:task_index>', methods=['POST'])
def delete_task(username, task_index):
    tasks_file_path = f"{username}_tasks.json"

    if os.path.exists(tasks_file_path):
        with open(tasks_file_path, 'r') as file:
            tasks_data = json.load(file)
    else:
        tasks_data = []
    
    tasks_data.pop(task_index)

    with open(tasks_file_path, 'w') as file:
        json.dump(tasks_data, file)

    return redirect(url_for('home.home', username=username))