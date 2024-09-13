from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configuración de la base de datos
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''  # Asegúrate de que esta es la contraseña correcta
app.config['MYSQL_DB'] = 'sitio'

# Inicializa la extensión MySQL
mysql = MySQL(app)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/libros')
def libros():
    return render_template('sitio/libros.html')

@app.route('/nosotros')
def nosotros():
    return render_template('sitio/nosotros.html')

@app.route('/admin/')
def admin_index():
    return render_template("admin/index.html")

@app.route('/admin/login')
def admin_login():
    return render_template("admin/login.html")

@app.route('/admin/libros')
def admin_libros():
    try:
        # Obtén la conexión
        conexion = mysql.connection
        print("Conexión a MySQL establecida.")
        
        # Aquí puedes hacer consultas a la base de datos si es necesario
        # Por ejemplo, puedes obtener datos de una tabla
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM libros")  # Asegúrate de que la tabla 'libros' exista
        data = cursor.fetchall()
        cursor.close()
        
        # Pasar datos al template si es necesario
        return render_template("admin/libros.html", libros=data)
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/admin/libros/guardar', methods=['POST'])
def admin_libros_guardar():
    _Nombre = request.form.get('textNombre')
    _URL = request.form.get('textURL')
    _archivo = request.files.get('textImagen')
    
    print(_Nombre)
    print(_URL)
    print(_archivo)
  
    # Aquí podrías guardar los datos en la base de datos
    try:
        conexion = mysql.connection
        cursor = conexion.cursor()
        # Asumiendo que tienes una tabla llamada 'libros' con las columnas adecuadas
        cursor.execute("INSERT INTO libros (nombre, url, imagen) VALUES (%s, %s, %s)", (_Nombre, _URL, _archivo.filename))
        conexion.commit()
        cursor.close()
    except Exception as e:
        return f"Error al guardar los datos: {str(e)}"

    return redirect('/admin/libros')

if __name__ == '__main__':
    app.run(debug=True)

