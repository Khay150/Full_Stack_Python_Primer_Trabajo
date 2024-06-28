from flask import Flask
from flask import render_template

# Creamos la aplicación
app = Flask(__name__)
# Proporcionamos la ruta a la raiz del sitio
@app.route('/')
def index():
    return render_template(
        'templates\index.html')



if (__name__=="__main__"):
    app.run(debug=True)