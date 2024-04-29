from flask import Flask, render_template
from . import home
from . import auth


def create_app():
    app = Flask(__name__)  # Crea una instancia de la aplicación Flask
    
    # Configuración de la aplicación
    app.config.from_mapping(
        DEBUG = True,        # Activa el modo de depuración para la aplicación
        SECRET_KEY = 'Dev'   # Clave secreta utilizada para proteger las sesiones y datos
    )
    
    # Ruta para la URL raíz@app.route('/')
    @app.route('/')
    def index():
        return render_template('index.html')
      # Renderiza la plantilla 'index.html'

    #Registro de BluePrint
    app.register_blueprint(home.bp)  # Registra un Blueprint llamado 'homeworks'
    app.register_blueprint(auth.bp)       # Registra un Blueprint llamado 'auth'
    return app  # Devuelve la instancia de la aplicación Flask configurada
