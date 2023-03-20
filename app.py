from flask import Flask
from flask import render_template
from flask import send_from_directory

app = Flask(__name__)

@app.route("/css/<archivo>")
def css_archivo(archivo):
    import os
    return send_from_directory(os.path.join('templates/sitio/css'), archivo)

@app.route('/logos/<logo>')
def logo_skills(logo):
    import os
    return send_from_directory(os.path.join('templates/sitio/logos'), logo)
    
@app.route("/img/<imagenes>")
def imagenes(imagenes):
    import os
    return send_from_directory(os.path.join('templates/sitio/img'), imagenes)

@app.route('/')
def inicio():
    return render_template('sitio/index.html')

@app.route('/skills')
def skills():
    return render_template('sitio/skills.html')

@app.route('/educacion')
def educacion():
    return render_template('sitio/educacion.html')

@app.route('/contacto')
def contracto():
    return render_template('sitio/contacto.html')

@app.route('/sobremi')
def sobre_mi():
    return render_template('sitio/sobre-mi.html')

if __name__ == '__main__':
    app.run(debug=True)