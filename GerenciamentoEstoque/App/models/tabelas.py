from App.models import db


class Login(db.Model):
    __nometabela__ = "cadastros"

    username = db.Column(db.String, unique=True)
    senha = db.Column(db.String)

    def __init__(self, username, senha):
        self.username = username
        self.senha = senha

    def __repr__(self):
        return "<Usuario: %r>" % self.username


class Estoque(db.Model):
    __nometabela = "estoques"

    id = db.Column(db.Integer, primary_key=True)
    NomeProduto = db.Column(db.String, unique=True)
    Quantidade = db.Column(db.Integer)

    def __init__(self, id, NomeProduto, Quantidade):
        self.id = id
        self.NomeProduto = NomeProduto
        self.Quantidade = Quantidade

    def __repr__(self):
        return "<Produto: %r>" % self.NomeProduto
