from flask import Flask
from flask import render_template
import requests
import json

app = Flask(__name__, template_folder='templates')


@app.route("/")
def get_locales_comida():
    r = requests.get("http://localhost:8000/api/locales_comidas/",
              auth=('roger1234', '1'))
    data = json.loads(r.content)
    return render_template("listarlocalescomida.html", data=data)

@app.route("/locales_repuestos")
def get_locales_repuestos():
    r = requests.get("http://localhost:8000/api/locales_repuestos/",
             auth=('roger1234', '1'))
    data = json.loads(r.content)
    return render_template("listarlocalesrepuestos.html", data=data)


@app.route("/barrios")
def get_barrios():
    r = requests.get("http://localhost:8000/api/barrios/",
            auth=('roger1234', '1'))
    data = json.loads(r.content)
    return render_template("listarbarrios.html", data=data)


@app.route("/personas")
def get_personas():
    data = requests.get("http://localhost:8000/api/personas/",
             auth=('roger1234', '1'))
    data = json.loads(data.content)
    return render_template("personas.html", data=data)

app.run()
