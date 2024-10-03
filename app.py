from flask import (Flask, request) #Importa o flask

app = Flask(__name__) #Cria uma instância

@app.route("/", methods=('GET' ,)) #Assina uma rota
def index (): #Função responsavel pela página
    nome = request.args.get('nome')
    #HTML retornado
    return f"""<h1>Pagina Inicial</h1> <p>Eu sou Mary</p>
    <p>Olá {nome}, que nome bonito!<p>
    """

@app.route("/galeria", methods=('GET',))
def galeria():
    return "<h1>GALERIA</h1>" 

@app.route("/contato", methods=('GET',))
def contato():
    return "<h1>CONTATO</h1>" 

@app.route("/sobre", methods=('GET',))
def sobre():
    return "<h1>Sobre...</h1>" 
    