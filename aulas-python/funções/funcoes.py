# ESTUDO APROFUNDADO SOBRE FUNÇÕES

"""O QUE SÇAO FUNÇÕES: É UM BLOCO DE CÓDIGO IDENTIFICADO POR UM NOME E PODE RECEBER UMA LISTA DE PARÂMETROS, ESSES PARÂMETROS PODEM OU NÃO TER VALORES PADROES. 

USAR FUNÇÕES TORNA O CÓDIGO MAIS LEGIVEL E POSSIBILITA O REAPROVEITAMENTO DE CÓDIGO. PROGRAMAR BASEADO EM FUNÇÕES, É O MESMO QUE DIZER QUE ESTAMOS PROGRAMANDO DE MANEIRA ESTRUTURADA

OU SEJA, Funções em Python (e em qualquer linguagem de programação) são blocos de código reutilizáveis que executam uma tarefa específica. Elas servem para organizar melhor o código, evitar repetições e facilitar a manutenção.

Uma função é como uma máquina de suco: você coloca frutas (valores), ela faz o processo (o código dentro da função) e te entrega um suco (o resultado). E você pode usar essa máquina quantas vezes quiser, mudando as frutas, sem precisar construir a máquina de novo toda vez!"""

print()
print(" Funções ".center(30, "="))

def exibir_mensagem():
    print("Olá mundo!")

def exibir_mensagem_2(nome): # como aqui eu não passei o valor pra nome eu tenho que passar quando a função for chamada
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem_3(nome="Anônomo"): # Nesse cadso se ao chamar a função eu não passer nenhum valor ele vi usar o valor determinado na função. mas se eu passr um valor ao chamar a função então valerá o novo valor.
    print(f"Seja bem vindo {nome}!")
    
exibir_mensagem()
exibir_mensagem_2(nome="Éveli")
exibir_mensagem_2("Éveli")
exibir_mensagem_3()
exibir_mensagem_3(nome="Éveli Lima")

def linha(tema):
    print()
    print(tema.center(30, "="))

linha(tema="Retornando valores")

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

linha(tema="Argumentos nomeados")

"""FUNÇÕES TAMBÉM PODEM SER CHAMADAS USANDO ARGUMENTOS NOMEADOS DA FORMA CHAVE=VALOR"""

def salvar_carro(marca, modelo, ano, placa): # Salva carro no banco de dados
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})

linha(tema="Args e Kwargs")

"""PODEMOS COMBINAR PARÂMETROS OBRIGATÓRIOS COM ARGS E KWARGS. QUANDO ESSES SÃO DEFINIDOS(*ARGS E *KWARGS), O MÉTODO RECENE OS VALORES COMO TUPLA E DICIONÁRIO RESPECTIVAMENTE."""

def exibir_poema(data_extenso, *args, **kwargs):
    texto ="\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema("Terça feira, 15 de Julho de 2025", "Zen of Python", "Beautiful is better than ugly.", autor="Tim Peters", ano=1999)