#Modelos de Data
import os
import json

def create_user(username, password):
    # Verificar si el usuario ya existe
    users_file_path = "users.json" #Si no le digo ruta se guarda en en mismo archivo run 
    if os.path.exists(users_file_path):
        with open(users_file_path, 'r') as file:
            users_data = json.load(file)
    else:
        users_data = []

    # Verificar si el usuario ya existe
    for user in users_data:
        if user['username'] == username:
            return False
            #message_verify = "El usuario ya existe. Por favor, elige otro nombre de usuario."
            #return render_template('register.html', message_verify=message_verify)

        # Agregar el nuevo usuario a la lista de usuarios
    new_user = {'username': username, 'password': password}
    users_data.append(new_user)

        # Guardar la lista actualizada de usuarios en el archivo JSON
    with open(users_file_path, 'w') as file:
        json.dump(users_data, file)
    return True