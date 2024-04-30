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

        
        users_file_path = "users.json" #Si no le digo ruta se guarda en en mismo archivo run 
        if os.path.exists(users_file_path):
            with open(users_file_path, 'r') as file:
                users_data = json.load(file)
        else:                                                   
            users_data = []                                                                                                                          

        # Verificar si el usuario ya existe    
        for user in users_data:
            if user['username'] == username:
                #return False
                message_verify = "El usuario ya existe. Por favor, elige otro nombre de usuario."
                return render_template('register.html', message_verify=message_verify)
            else:
                new_user = {'username': username, 'password': password}
                users_data.append(new_user)
                message_verify = "Creacion de usuario correctamente."
                with open(users_file_path, 'w') as file:
                    json.dump(users_data, file)
                return render_template('register.html', message_verify=message_verify)
            # Agregar el nuevo usuario a la lista de usuarios
        

        # Guardar la lista actualizada de usuarios en el archivo JSON
        
        
    
    
        return render_template('register.html')

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
        for user in users_data:
                #Autenticación de usuario
                if user['username'] == username and user['password'] == password:
                    # Usuario autenticado correctamente, redirigir a la página de inicio
                    return redirect(url_for('home.home',username=username))
                elif user['username'] != username or user['password'] != password:
                    message = "Verifica tus datos"
                    return render_template('login.html', message = message)
        
    return render_template('login.html')