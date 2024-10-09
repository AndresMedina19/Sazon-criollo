from flask import Flask, request, jsonify
import psycopg2
import bcrypt

app = Flask(__name__)

# Conexión a la base de datos PostgreSQL
def get_db_connection():
    conn = psycopg2.connect(
        dbname="registro_db", user="postgres", password="postgres", host="localhost"
    )
    return conn

# Ruta para registrar usuarios
@app.route('/registro', methods=['POST'])
def registrar_usuario():
    data = request.json
    nombre = data.get('nombre')
    celular = data.get('celular')
    tipo_documento = data.get('tipo_documento')
    numero_documento = data.get('numero_documento')
    contrasena = data.get('contrasena')

    # Cifrar la contraseña con bcrypt
    hashed_password = bcrypt.hashpw(contrasena.encode('utf-8'), bcrypt.gensalt())

    conn = get_db_connection()
    cur = conn.cursor()

    try:
        # Insertar datos en la tabla
        cur.execute(
            """
            INSERT INTO tab_usuarios (nombre, celular, tipo_documento, numero_documento, contrasena)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (nombre, celular, tipo_documento, numero_documento, hashed_password)
        )
        conn.commit()
        return jsonify({"success": True})
    
    except Exception as e:
        conn.rollback()
        return jsonify({"success": False, "error": str(e)})

    finally:
        cur.close()
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
