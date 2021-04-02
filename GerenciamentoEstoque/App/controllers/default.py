from flask import render_template
from App.controllers import app


@app.route('/login')
@app.route('/')
def Login():
    return """
<html>
    <head>
        <title>Gerenciador de Estoque</title>
    </head>
    <body>
         <h1>Login</h1>
    </body>
</html>   
    """
