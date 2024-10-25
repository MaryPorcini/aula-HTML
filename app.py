from flask import (Flask, render_template, request) #Importa o flask

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
@app.route("/numero/<float:parimpar>", methods=('GET',))
def numero(parimpar: float):
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

# 17/10
# Potencia
@app.route("/potencia/<float:numero>/<float:elevado>", methods=('GET',))
def potencia(numero: float, elevado: float):
    return f"""<h1>A potencia é> N={numero}* E={elevado} => Potencia={numero*elevado}</h1>"""

# 18/10
# Tabuada
@app.route("/tabuada")
@app.route("/tabuada/<numero>", methods=("GET", ))
def tabuada(numero = None):

  if 'numero' in request.args:
    numero = int(request.args.get('numero'))
  
  return render_template('tabuada.html',numero=numero)

# 25/10
# Calculo do juros
@app.route('/juros', methods=['GET', 'POST'])
def juros():
    if request.method == 'POST':
        try:
            investimento_inicial = float(request.form['investimento_inicial'])
            juros_ano = float(request.form['juros_ano'])
            tempo_meses = int(request.form['tempo_meses'])
            aporte_mensal = float(request.form['aporte_mensal'])

            juros_mensal = juros_ano / 12 / 100
            total = investimento_inicial

            for _ in range(tempo_meses):
                total += aporte_mensal
                total *= (1 + juros_mensal)

            return render_template('juros.html', total=total)
        except ValueError:
            return render_template('juros.html', error="Por favor, insira valores válidos.")

    return render_template('juros.html')



# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        
        # Verificação de credenciais
        if email == 'aluno@senai.br' and senha == 'senai':
            flash('Usuário Logado com Sucesso!', 'success')
            return redirect(url_for('login'))
        else:
            flash('Usuário ou senha incorretos, tente novamente.', 'error')

    return render_template('login.html')



# Calculo do IMC
@app.route('/imc', methods=['GET', 'POST'])
def imc():
    imc = None
    categoria = None

    if request.method == 'POST':
        peso = float(request.form['peso'])
        altura = float(request.form['altura'])
        imc = peso / (altura ** 2)

        if imc < 18.5:
            categoria = 'Magreza'
        elif imc < 24.9:
            categoria = 'Normal'
        elif imc < 29.9:
            categoria = 'Sobrepeso - Grau 1'
        elif imc <39.9:
            categoria = 'Obesidade - Grau 2'
        else:
            categoria = 'Obesidade Grave - Grau 3'

    return render_template('imc.html', imc=imc, categoria=categoria)
