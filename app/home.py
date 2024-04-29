from flask import Blueprint, render_template, request, redirect, url_for
import json
import os

bp = Blueprint('home',__name__)



@bp.route('/home', methods=['GET', 'POST'])
def home():
    username = request.args.get('username')
    tasks_file_path = f"{username}_tasks.json" 

    tasks_data = []  # Inicializar tasks_data fuera de los bloques if y else
    
    if request.method == 'POST':
        task = request.form.get('task')
        date = request.form.get('date')
        if task and date:
            if os.path.exists(tasks_file_path):
                with open(tasks_file_path, 'r') as file:
                    tasks_data = json.load(file)
            else:
                tasks_data = []

            new_task = {'task': task, 'date': date}
            tasks_data.append(new_task)

            with open(tasks_file_path, 'w') as file:
                json.dump(tasks_data, file)
    
    else:
        if os.path.exists(tasks_file_path):
            with open(tasks_file_path, 'r') as file:
                tasks_data = json.load(file)
    print(tasks_data)

    return render_template('home.html', username=username, tasks=tasks_data)


