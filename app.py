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


# Dia 11/10
# Multiplicação
@app.route("/area/<float:altura>/<float:largura>", methods=('GET',))
def area(altura: float, largura: float):
    return f"""<h1>A área informada> L={largura}*A={altura} => Área={largura*altura}</h1>"""

# Número Par ou Impar
@app.route("/numero", methods=('GET',))
def numero():
  numero = float(request.args.get('n'))
  if numero % 2 == 0:
    return f"O número é par."
  else:
    return f"O número é ímpar."

# Nome e Sobrenome 
@app.route("/nome", methods=('GET',))
def nome():
  nome = request.args.get('nome')
  sobrenome = request.args.get('sobrenome')
  return f"""<h1> Resultado </h1>
  <p>{sobrenome},{nome}</p>"""