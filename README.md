<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Asistencia Semanal</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 0;
            background: #f5f5f5;
        }
        .section {
            margin: 20px auto;
            width: 90%;
            max-width: 800px;
            background-color: rgba(255, 255, 255, 0.9);
            border-radius: 20px;
            padding: 20px;
            position: relative;
            overflow: hidden;
        }
        .section::before {
            content: "";
            position: absolute;
            top: 0; left: 0;
            width: 100%; height: 100%;
            background-size: cover;
            background-position: center;
            opacity: 0.5;
            z-index: 0;
        }
        .inicial::before {
            background-image: url('/static/samus.jpg');
        }
        .primaria::before {
            background-image: url('/static/kanade.jpg');
        }
        .content {
            position: relative;
            z-index: 1;
        }
        input[type="number"] {
            width: 60px;
            padding: 5px;
            border-radius: 10px;
            border: 1px solid #ccc;
            text-align: center;
            transition: background-color 0.3s;
        }
        input[type="number"]:hover {
            background-color: #e0f0ff;
        }
        button {
            padding: 10px 20px;
            margin-top: 15px;
            border-radius: 15px;
            background-color: #4CAF50;
            color: white;
            border: none;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #45a049;
        }
        h2 {
            margin-top: 0;
        }
        table {
            margin: auto;
            border-collapse: collapse;
        }
        td, th {
            padding: 8px 12px;
        }
    </style>
</head>
<body>
    <h1>Registro de Asistencia</h1>
    <form method="post">
        <div class="section inicial">
            <div class="content">
                <h2>Inicial</h2>
                <table>
                    <tr>
                        <th>Día</th><th>Asistencia</th><th>%</th>
                    </tr>
                    {% for dia in datos["Inicial"] %}
                    <tr>
                        <td>{{ dia.capitalize() }}</td>
                        <td><input type="number" name="Inicial_{{ dia }}" value="{{ datos['Inicial'][dia] }}"></td>
                        <td>{{ porcentajes['Inicial'][dia] }}%</td>
                    </tr>
                    {% endfor %}
                </table>
                <p>Promedio Semanal: {{ total_porcentaje['Inicial'] }}%</p>
            </div>
        </div>
        <div class="section primaria">
            <div class="content">
                <h2>Primaria</h2>
                <table>
                    <tr>
                        <th>Día</th><th>Asistencia</th><th>%</th>
                    </tr>
                    {% for dia in datos["Primaria"] %}
                    <tr>
                        <td>{{ dia.capitalize() }}</td>
                        <td><input type="number" name="Primaria_{{ dia }}" value="{{ datos['Primaria'][dia] }}"></td>
                        <td>{{ porcentajes['Primaria'][dia] }}%</td>
                    </tr>
                    {% endfor %}
                </table>
                <p>Promedio Semanal: {{ total_porcentaje['Primaria'] }}%</p>
            </div>
        </div>
        <div class="boton-container">
            <button type="submit">Calcular</button>
            <button type="submit" name="reset">Restablecer</button>
            
        </div>
    </form>
</body>
</html>
