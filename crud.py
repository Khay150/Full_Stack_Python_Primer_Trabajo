from flask import Flask
from flask import render_template, request, redirect, url_for
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
    
    return render_template('index.html')

@app.route('/index.html')
def redirect_to_index():
    return redirect(url_for('index'))

#pagina catalogo
@app.route('/Catalogo.html')
def Catalogo():
    return render_template('Catalogo.html')


#pagina notalogo
@app.route('/nosotros.html')
def Nosotros():
    return render_template('nosotros.html')


#pagina FAQ
@app.route('/FQ.html')
def FAQ():
    return render_template('FQ.html')

#pagina con la BD
@app.route('/datos.html')
def datos():
    sql = "SELECT * FROM `libros`.`catalogo`;"

    # Nos conectamos a la base de datos
    conn = mysql.connect()
    # Sobre el cursor vamos a realizar las operaciones
    cursor = conn.cursor()
    # Ejecutamos la sentencia SQL sobre el cursor
    cursor.execute(sql)
    # Copiamos el contenido del cursor a una variable
    db_libros = cursor.fetchall()
    # y mostramos las tuplas por la terminal
    print("-"*60)
    for libro in db_libros:
        print(libro)
    print("-"*60)

    # "Commiteamos" (Cerramos la conexión)
    conn.commit()
    # Devolvemos código HTML para ser renderizado
    return render_template('datos.html', c = db_libros)

# Destroy
# Función para eliminar un registro
@app.route('/destroy/<int:id>')
def destroy(id):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM `libros`.`catalogo` WHERE id_libro=%s", (id))
    conn.commit()
    return redirect(url_for('datos'))

# Función para editar un registro
@app.route('/edit/<int:id>')
def edit(id):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM `libros`.`catalogo` WHERE id_libro=%s", (id))
    datos = cursor.fetchall()
    conn.commit()
    return render_template('edit.html', d = datos)


# Función para actualizar los datos de un registro
@app.route('/update', methods=['POST'])
def update():
    
    
    _titulo = request.form['titulo_del_libro']
    _titulo_original = request.form['titulo_original']
    _autor = request.form['autor']
    _genero = request.form['genero']
    _publicacion = request.form['publicacion']
    
    id=request.form['txtID']
    
    
    sql = "UPDATE `libros`.`catalogo` SET `titulo_libro`=%s, `titulo_original`=%s, `autor`=%s, `genero`=%s, `publicacion`=%s WHERE id_libro=%s;"
    datos = (_titulo, _titulo_original, _autor, _genero, _publicacion, id)
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    return redirect(url_for('datos'))


# Create
@app.route('/create')
def create():
    return render_template('create.html')

# Store
@app.route('/store', methods =['POST'])
def storage():
    # Recibimos los valores del formulario:
    _titulo = request.form['titulo_del_libro']
    _titulo_original = request.form['titulo_original']
    _autor = request.form['autor']
    _genero = request.form['genero']
    _publicacion = request.form['publicacion']

    # Armamos una tupla con los valores
    datos = (_titulo, _titulo_original, _autor, _genero, _publicacion)

    # Armamos la sentencia SQL que almacena eso datos en la BD
    sql = "INSERT INTO `libros`.`catalogo` (`titulo_libro`, `titulo_original`, `autor`, `genero`, `publicacion`)\
         VALUES (%s, %s, %s, %s, %s);"

    # Conectamos a la BD
    conn = mysql.connect()

    # Creamos el cursor
    cursor = conn.cursor()

    # Ejecutamos la sentencia SQL
    cursor.execute(sql, datos)

    # Commiteamos (Cerramos la conexion)
    conn.commit()

    return redirect(url_for('datos'))
    


#pagina catalogo
@app.route('/prueba.html')
def prueba():
    return render_template('prueba.html')


if (__name__=="__main__"):
    app.run(debug=True)

