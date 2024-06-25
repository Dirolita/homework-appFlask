from flask import Blueprint, render_template, request, redirect, url_for, flash
from . import models
import os
import json


bp = Blueprint('auth',__name__, url_prefix='/')

@bp.route('/register',  methods=['GET', 'POST'])
def register():
   if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        message_verify_exist = ""
        message_verify = ""

        users_file_path = "users.json"
        
        # Cargar usuarios existentes
        if os.path.exists(users_file_path):
            with open(users_file_path, 'r') as file:
                users_data = json.load(file)
        else:
            users_data = []

        # Verificar si el usuario ya existe
        user_exists = any(user['username'] == username for user in users_data)
        
        if user_exists:
            message_verify_exist = "El usuario ya existe. Por favor, elige otro nombre de usuario."
            return render_template('register.html', message_verify_exist=message_verify_exist)
        
        # Añadir nuevo usuario
        new_user = {'username': username, 'password': password}  # Considera el hashing para la contraseña
        users_data.append(new_user)

        # Guardar el nuevo usuario
        with open(users_file_path, 'w') as file:
            json.dump(users_data, file)
        
        message_verify = "Usuario creado correctamente."
        return render_template('register.html', message_verify=message_verify)

        


   #redirect(url_for('auth.login', message=message))

   return render_template('register.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        message = ""
        users_file_path = "users.json"
        if os.path.exists(users_file_path):
            with open(users_file_path, 'r') as file:
                users_data = json.load(file)
        else:
            message = "La Base de datos no existe"
            return render_template('login.html', message=message)
        user_found = None
        for user in users_data:
            if user['username'] == username:
                user_found = user
                break
        
        if user_found and user_found['password'] == password:
            # Usuario autenticado correctamente
            return redirect(url_for('home.home', username=username))
        else:
            # Credenciales incorrectas
            message = "Verifica tus datos."
            return render_template('login.html', message=message)
        
    return render_template('login.html')