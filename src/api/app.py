from flask import app, Flask, render_template

app = Flask(__name__)


@app.route('/')
def inicio():
    tittle= "início"
    return render_template('inicio.html', titulo=tittle)

@app.route('/Projetos')
def Projetos():
    tittle='Projetos'
    return render_template('Projetos.html', titulo=tittle)

@app.route('/Sobremim')
def Sobremim():
    tittle='Sobre mim'
    return render_template('Sobre mim.html', titulo=tittle)

@app.route('/Contatos')
def Contatos():
    tittle='Contatos'
    return render_template('Contatos.html', titulo=tittle)

if __name__ == '__main__':
    app.run('0.0.0.0')