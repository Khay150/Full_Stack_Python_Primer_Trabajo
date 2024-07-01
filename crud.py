from flask import Flask
from flask import render_template
from flaskext.mysql import MySQL

# Creamos la aplicación
app = Flask(__name__)

# Creamos la conexion con la base de 
mysql = MySQL()

# Creamos la referencia al host, para que se conece a la base de datos MySQL utilizamos el localhost
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

# Indicamos el usuario
app.config['MYSQL_DATABASE_USER'] = 'root'



# Nombre de nuestra BD
app.config['MYSQL_DATABASE_BD'] = 'libros'

# Creamos la conexion con los datos
mysql.init_app(app)


# Proporcionamos la ruta a la raiz del sitio
@app.route('/')
def index():
    return render_template(
        'index.html')
#pagina catalogo
@app.route('/Catalogo.html')
def Catalogo():
    return render_template(
        'Catalogo.html')

#pagina notalogo
@app.route('/nosotros.html')
def Nosotros():
    return render_template(
        'nosotros.html')
#pagina FAQ
@app.route('/FQ.html')
def FAQ():
    return render_template(
        'FQ.html')

#pagina prueba
@app.route('/prueba.html')
def prueba():
    # Creamos una variables que va a contener las consulta sql
    sql = "INSERT INTO `libros`.`catalogo` (`titulo_libro`, `titulo_original`, `autor`, `genero`, `publicacion`)\
         VALUES ('La Asistenta', 'The Housemaid', 'Freida McFadden', 'Thriller psicológico, Suspense', 2022); "
    
    # Conectamos a la conexion mysql.init_app(app)
    conn = mysql.connect()

    # Almacenamos lo que devuelva la consulta
    cursor = conn.cursor()

    # Ejecutamos la sentencia SQL
    cursor.execute(sql)

    # Commiteamos (Cerramos la conexion)
    conn.commit()

    return render_template(
        'prueba.html')





if (__name__=="__main__"):
    app.run(debug=True)

