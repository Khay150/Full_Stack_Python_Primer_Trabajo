from flask import Flask
from flask import render_template
from flaskext.mysql import MySQL

# Creamos la aplicación
app = Flask(__name__)
# Proporcionamos la ruta a la raiz del sitio
@app.route('/index.html')
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

if (__name__=="__main__"):
    app.run(debug=True)