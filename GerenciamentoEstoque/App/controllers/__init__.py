from flask import Flask

app = Flask(__name__)


@app.route('/estoque')
def ControleEstoque():
    return "Estoque"


@app.route('/cadastro')
def CadastroProduto():
        return "Cadastro"


@app.route('/excluir')
def ExcluirProduto():
    return "Excluír!"


if __name__ == '__main__':
    app.run()
