"""No arquivo de rota do Flask, renderizei o template usando a função render_template do Flask. Inseri o nome do
arquivo de template como argumento.
"""
from flask import Flask, render_template

aplicacao = Flask(__name__)


@aplicacao.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    aplicacao.run(debug=True)
