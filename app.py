from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)
DATA_FILE = 'data.json'
TOTAL_INICIAL = 17
TOTAL_PRIMARIA = 55

def cargar_datos():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    else:
        return {
            "Inicial": {"lunes": 0, "martes": 0, "miércoles": 0, "jueves": 0, "viernes": 0},
            "Primaria": {"lunes": 0, "martes": 0, "miércoles": 0, "jueves": 0, "viernes": 0}
        }

def guardar_datos(datos):
    with open(DATA_FILE, 'w') as f:
        json.dump(datos, f)

@app.route('/', methods=['GET', 'POST'])
def index():
    datos = cargar_datos()

    if request.method == 'POST':
        if 'reset' in request.form:  # Verifica si el botón "Restablecer" fue presionado
            datos = {
                "Inicial": {"lunes": 0, "martes": 0, "miércoles": 0, "jueves": 0, "viernes": 0},
                "Primaria": {"lunes": 0, "martes": 0, "miércoles": 0, "jueves": 0, "viernes": 0}
            }
            guardar_datos(datos)
            return redirect('/')
        else:  # Actualiza los valores del formulario
            for nivel in ["Inicial", "Primaria"]:
                limite = TOTAL_INICIAL if nivel == "Inicial" else TOTAL_PRIMARIA
                for dia in ["lunes", "martes", "miércoles", "jueves", "viernes"]:
                    valor = request.form.get(f"{nivel}_{dia}", 0)
                    valor = int(valor) if valor.isdigit() else 0
                    datos[nivel][dia] = min(valor, limite)  # Ajusta al máximo permitido
            guardar_datos(datos)
            return redirect('/')

    porcentajes = {"Inicial": {}, "Primaria": {}}
    total_porcentaje = {"Inicial": 0, "Primaria": 0}
    for nivel in ["Inicial", "Primaria"]:
        total_nivel = TOTAL_INICIAL if nivel == "Inicial" else TOTAL_PRIMARIA
        for dia, asistencia in datos[nivel].items():
            porcentaje = round(asistencia / total_nivel * 100, 2)
            porcentajes[nivel][dia] = porcentaje
            total_porcentaje[nivel] += porcentaje
        total_porcentaje[nivel] = round(total_porcentaje[nivel] / 5, 2)

    return render_template("formulario.html", datos=datos, porcentajes=porcentajes, total_porcentaje=total_porcentaje)

if __name__ == '__main__':
    app.run(debug=True)
