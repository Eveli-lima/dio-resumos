# ESTUDO APROFUNDADO SOBRE FUNÇÕES

"""O QUE SÇAO FUNÇÕES: É UM BLOCO DE CÓDIGO IDENTIFICADO POR UM NOME E PODE RECEBER UMA LISTA DE PARÂMETROS, ESSES PARÂMETROS PODEM OU NÃO TER VALORES PADROES. 

USAR FUNÇÕES TORNA O CÓDIGO MAIS LEGIVEL E POSSIBILITA O REAPROVEITAMENTO DE CÓDIGO. PROGRAMAR BASEADO EM FUNÇÕES, É O MESMO QUE DIZER QUE ESTAMOS PROGRAMANDO DE MANEIRA ESTRUTURADA

OU SEJA, Funções em Python (e em qualquer linguagem de programação) são blocos de código reutilizáveis que executam uma tarefa específica. Elas servem para organizar melhor o código, evitar repetições e facilitar a manutenção.

Uma função é como uma máquina de suco: você coloca frutas (valores), ela faz o processo (o código dentro da função) e te entrega um suco (o resultado). E você pode usar essa máquina quantas vezes quiser, mudando as frutas, sem precisar construir a máquina de novo toda vez!"""

print()
print(" Funções ".center(40, "="))

def exibir_mensagem():
    print("Olá mundo!")

def exibir_mensagem_2(nome): # como aqui eu não passei o valor pra nome eu tenho que passar quando a função for chamada
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem_3(nome="Anônomo"): # Nesse caso se ao chamar a função eu não passar nenhum valor ele vai usar o valor determinado na função. mas se eu passar um valor ao chamar a função então valerá o novo valor.
    print(f"Seja bem vindo {nome}!")
    
exibir_mensagem()
exibir_mensagem_2(nome="Éveli")
exibir_mensagem_2("Éveli")
exibir_mensagem_3()
exibir_mensagem_3(nome="Éveli Lima")

def linha(tema):
    print()
    print(tema.center(40, "="))

linha(tema=" Retornando valores ")

"""PARA RETORNAR UM VALOR, UTILIZAMOS A PALAVRA RESERVADA RETURN. TODA FUNÇÃO PYTHON RETORNA NONE POR PADRÃO. EM PYTHON UMA FUNÇÃO PODE RETORNAR MAIS DE UMA VALOR"""

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor # ele retorna uma tupla pois é uma estrutura imutável

def func_3():
    print("Olá Mundo!")
    #return None -> posso colocar ou não.

print(calcular_total([10, 20, 34]))
print(retorna_antecessor_e_sucessor(10))
print(func_3()) # retorna none por padrão

linha(tema=" Argumentos nomeados ")

"""FUNÇÕES TAMBÉM PODEM SER CHAMADAS USANDO ARGUMENTOS NOMEADOS DA FORMA CHAVE=VALOR"""

def salvar_carro(marca, modelo, ano, placa): # Salva carro no banco de dados
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"}) # ** Dicionário

linha(tema=" Args e Kwargs ")

"""PODEMOS COMBINAR PARÂMETROS OBRIGATÓRIOS COM ARGS E KWARGS. QUANDO ESSES SÃO DEFINIDOS(*ARGS E **KWARGS), O MÉTODO RECENE OS VALORES COMO TUPLA E DICIONÁRIO RESPECTIVAMENTE."""

def exibir_poema(data_extenso, *args, **kwargs): # no lugar de *args e **kwargs pode ser qualquer valor tipo *lista, **dicionário.
    texto ="\n".join(args) #lista
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()]) # dicionário no lugar de kwargs
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema(
    "Terça feira, 15 de Julho de 2025", # a primeira linha sempre será considerada uma data por extenso

    "Zen of Python", # valores separados por virgulas dentro de um parênteses é uma tupla ou *args
    "Beautiful is better than ugly.", 

    autor="Tim Peters", # Quando acabar os valores separados por virgulas e começar os de chave e valor ele vai considerar um dicionário ou **kwargs
    ano=1999)

linha(tema=" Parâmetros especiais ")

"""POR PADRÃO, ARGUMENTOS PODEM SER PASSADOS PARA UMA FUNÇÃO pYTHON TANTO POR POSIÇÃO QUANTO POR EXPLICITAMENTE PELO NAOME. PARA MELHOR LEGIBILIDADE E DESENPENHO, FAZ SENTIDO RESTRINGIR A MANEIRA PELO QUAL ARGUMENTOS POSSAM SER PASSADOS ASSIM UM DESENVOLVEDOR PRECISA APENAS OLHAR PARA A DEFINIÇÃO DA FUNÇÃO PARA DETERMINAR SE OS ITENS SÃO PASSSADOS POR POSIÇÃO, POR POSIÇÃO E NOME, OU POR NOME."""

print("""
def f(pos1, pos2, /, pos or kwd, *, kwd1, kwd2):
      ----------     ----------     ----------
       |              |                  |
       |       positional or keyword     |
       |                                 - keyword only
        -- Positional only
""")

linha(tema=" Position only ")

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

    # Os primeiros, modelo, ano e placa, eu sou obrigada a passar sem as chaves, pois não são parâmetros nomeados. sou obrigado a passar somente por posição. os 3 últimos posso nomear as chaves ou não. pois depois da barra tem essas duas opções

criar_carro("Pálio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # válido

# criar_carro(modelo="Pálio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # inválido

linha(tema=" Keyword only ")

def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

    # Todos depois do asterisco é obrigatório colocar as chaves

criar_carro(modelo="Pálio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # válido

# criar_carro("Pálio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # inválido

linha(tema=" Keyword and positional only ")

def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Pálio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # válido

# criar_carro(modelo="Pálio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # inválido

linha(tema=" Objetos de primeira classe ")

"""EM PYTHON TUDO É UM OBJETO, DESSA FORMA FUNÇÕES TAMBÉM SÃO OBJETOS O QUE AS TORNAM OBJETOS DE PRIMERA CLASEE. COM ISSO PODEMOS ATRIBUIR FUNÇÕES A VARIÁVEIS, PASSA-LAS COMO PARÂMETRO PARA FUNÇÕES, USA-LAS COMO VALORES EM ESTRUTURAS DE DADOS (LISTAS, TUPLAS, DICIONÁRIOS, ETC) E USAR COMO VALOR DE RETORNO PARA UMA FUNÇÃO (CLOSURES)"""

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    if funcao == subtrair:
        print(f"O resultado da operação {a} - {b} = {resultado}")
    else:
        print(f"O resultado da operação {a} + {b} = {resultado}")


exibir_resultado(10, 10, somar)
exibir_resultado(15, 25, somar)
exibir_resultado(48, 37, subtrair)

op = somar
print(op(1, 23))

op = subtrair
print(op(48, 37))

linha(tema=" Escopo local e global ")

"""PYTHON TRABALHA COM ESCOPO LOCAL E GLOBAL, DENTRO DO BLOCO DA FUNÇÃO O ESCOPO É LOCAL. PORTANTO ALTERAÇÕES ALI FEITAS EM OBJETOS IMUTÁVEIS SERÃO PERDIDAS QUANDO O MÉTODO TERMINAR DE SER EXECUTADO. PARA USAR OBJETOS GLOBAIS UTILIZAMOS A PALAVRA-CHAVE GLOBAL, QUE INFORMA AO INTERPRETADOR QUE A VARIÁVEL QUE ESTÁ SENDO MANIPULADA NO ESCOPO LOCAL É GLOBAL. ❌ ESSA NÃO É UMA BOA PRÉTICA E DEVE SER EVITADA."""

salario = 2000 # Essa variável é de escopo global pois esta fora da minha função

def salario_bonus(bonus, lista):
    global salario # se eu quero utilizá-la eu tenho que informar que é global

    liat_aux = lista.copy() # eu tenho que fazer uma cópia para não alterar a referência externa
    liat_aux.append(2)
    print(f"lista aux = {liat_aux}")

    salario += bonus
    return salario

lista = [1] # argumento por referência externa que é um objeto mutável 
print(salario_bonus(500, lista))
print(lista)
