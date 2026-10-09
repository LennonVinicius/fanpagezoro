from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html', titulo='Início')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html', titulo='Sobre')

@app.route('/espadas')
def espadas():
    return render_template('espadas.html', titulo='Espadas')

@app.route('/galeria')
def galeria():
    return render_template('galeria.html', titulo='Galeria')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
