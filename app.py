from flask import Flask, request, render_template, jsonify
import sqlite3

app = Flask(__name__)

# Crear tabla si no existe
def crear_tabla():
    conn = sqlite3.connect('datos.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS datos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            categoria TEXT,
            cantidad INTEGER,
            fecha DATE
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guardar', methods=['POST'])
def guardar():
    categoria = request.form['categoria']
    cantidad = request.form['cantidad']
    fecha = request.form['fecha']

    conn = sqlite3.connect('datos.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO datos (categoria, cantidad, fecha) VALUES (?, ?, ?)', (categoria, cantidad, fecha))
    conn.commit()
    conn.close()
    return "Datos guardados con éxito"

@app.route('/datos')
def mostrar_datos():
    conn = sqlite3.connect('datos.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM datos')
    datos = cursor.fetchall()
    conn.close()
    return jsonify(datos)

if __name__ == "__main__":
    crear_tabla()
    app.run(debug=True)
