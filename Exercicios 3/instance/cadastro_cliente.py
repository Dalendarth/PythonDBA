from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cadastro.db'
db = SQLAlchemy(app)


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    senha = db.Column(db.String(50))


class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    endereco = db.Column(db.String(50))


from flask import render_template


@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')


@app.route('/')
def index():
    return 'Bem-vindo ao cadastro de clientes e usuários!'


@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([u.__dict__ for u in usuarios])


@app.route('/usuarios', methods=['POST'])
def create_usuario():
    data = request.get_json()
    novo_usuario = Usuario(nome=data['nome'], email=data['email'], senha=data['senha'])
    db.session.add(novo_usuario)
    db.session.commit()
    return jsonify(novo_usuario.__dict__)


@app.route('/clientes', methods=['GET'])
def get_clientes():
    clientes = Cliente.query.all()
    return jsonify([c.__dict__ for c in clientes])


@app.route('/clientes', methods=['POST'])
def create_cliente():
    data = request.get_json()
    novo_cliente = Cliente(nome=data['nome'], email=data['email'], endereco=data['endereco'])
    db.session.add(novo_cliente)
    db.session.commit()
    return jsonify(novo_cliente.__dict__)


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
