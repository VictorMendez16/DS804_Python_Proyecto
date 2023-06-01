from flask import Flask
from flask import request

app = Flask(__name__) # Instancia de flask llamada app


@app.route('/')  # Anotador para unicamente modificar el codigo sin tener que hacer una instancia de app
def hello():
    nombre = request.args.get('nombre')
    apellido = request.args.get('apellido')
    responseText = 'Hola {} {}!'.format(nombre, apellido)
    return responseText

@app.route('/help')
def help():
    return('Esta es la seccion de ayuda')