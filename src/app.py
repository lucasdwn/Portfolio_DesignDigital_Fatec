from flask import app, Flask, render_template

lfportfolio0804 = Flask(__name__)


@lfportfolio0804.route('/')
def inicio():
    tittle= "início"
    return render_template('inicio.html', titulo=tittle)

@lfportfolio0804.route('/Projetos')
def Projetos():
    tittle='Projetos'
    return render_template('Projetos.html', titulo=tittle)

@lfportfolio0804.route('/Sobremim')
def Sobremim():
    tittle='Sobre mim'
    return render_template('Sobremim.html', titulo=tittle)

@lfportfolio0804.route('/Contatos')
def Contatos():
    tittle='Contatos'
    return render_template('Contatos.html', titulo=tittle)

if __name__ == '__main__':
    lfportfolio0804.run('0.0.0.0')