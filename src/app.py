from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/Projetos')
def Projetos():
    return render_template('Projetos.html')

@app.route('/Sobremim')
def Sobremim():
    return render_template('Sobremim.html')

@app.route('/Contatos')
def Contatos():
    return render_template('Contatos.html')


app.run(debug=True)