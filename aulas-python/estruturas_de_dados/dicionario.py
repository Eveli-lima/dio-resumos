# DICIONÁRIOS - CRIAÇÃO E ACESSO AOS DADOS

'''É UM CONJUNTO NÃO ORDENADO DE PARES CHAVE:VALOR, ONDE AS CHAVES SÃO ÚNICAS EM UMA INSTÂNCIA DO DICIONÁRIO. DICIONÁRIOS SÃO DELIMITADOS POR CHAVES: {} OU DICT, E CONTÉM UMA LISTA DE PARES CHAVE:VALOR SEPARADA POR VÍRGULAS'''

# NA CHAVE DEVEMOS COLOCAR UM OBJETO IMUTÁVEL, EX.: TUPLA, STRING, PARA SER CONSIDERADO CHAVE NO PYTHON.

#O VALOR PODE SER QUALQUER TIPO DE OBJETO, PODE SER MUTÁVEL OU IMUTÁVEL

# DICIONÁRIOS

print()
print(" dicionário ".center(30, "="))

pessoa = {"nome": "Éveli", "idade": 28}
print(pessoa)

pessoa = dict(nome="Éveli", idade=28)
print(pessoa)

pessoa["telefone"] = "(21) 9999-9999" # acrescentando uma nova chave e atribuindo um novo valor.
print(pessoa)

# ACESSAR OS DADOS

print()
print(" acessar os dados ".center(30, "="))

# os dados são acessados e modificados através da chave

dados = {'nome': 'Éveli', 'idade': 28, 'telefone': '(21) 9999-9999'}
print(dados)


dados["nome"]
dados["idade"]
dados["telefone"]

# acima como não tem atribuição significa que eu estou tentando acessar o valor da chave. abaixo como tem atribuição significa que quero mudar o valor da chave.

dados["nome"] = "Maria"
dados["idade"] = 18
dados["telefone"] = "(33) 2222-2222"

print(dados)

# independente se vou ler ou acessar o valor da chave eu coloco assim => dados["nome"]


# DICIONÁRIOS ANINHADOS

'''DICIONÁRIOS PODEM ARMAZENAR QUALQUER TIPO DE OBJETO PYTHON COMO VALOR, DESDE QUE A CHAVE PARA ESSE VALOR SEJA UM OBJETO IMUTÁVEL COMO (STRINGS E NÚMEROS).'''

# O DICIONÁRIO TEM UMA ESTRUTURA MUITO PARECIDA COM BANCO DE DADOS
print()
print(" dicionários aninhados ".center(30, "="))

# abaixo temos um dicionário dento de outro o email é uma chave, nome e telefone tbm.

contatos = {
    "eveliazevedo@gmail.com": {'nome': 'Éveli', 'telefone': '(21) 9999-9999'},
    "fulana@gmail.com": {'nome': 'Fulana', 'telefone': '(21) 2222-2222'},
    "beutrana@gmail.com": {'nome': 'Beutrana', 'telefone': '(21) 3333-3333'},
    "cicrana@gmail.com": {'nome': 'Cicrana', 'telefone': '(21) 5555-5555', "extra": {"a": 1}},
}

#print(contatos["eveliazevedo@gmail.com"]["telefone"])
telefone = contatos["beutrana@gmail.com"]["telefone"]
print(telefone)

extra = contatos["cicrana@gmail.com"]
print(extra)

extra = contatos["cicrana@gmail.com"]["extra"]
print(extra)

extra = contatos["cicrana@gmail.com"]["extra"]["a"]
print(extra)

# ITERAR DICIONÁRIOS

'''A FORMA MAIS COMUM PARA PERCORRER OS DADOS DE UM DICIONÁRIO É UTILIZAR O COMANDO FOR'''

print()
print(" iterar ".center(30, "="))

for chave in contatos: # essa forma funciona mas não é a melhor, pois ele retorna só a primeira chave e vai descendo pra outras chaves.
    print(chave, contatos[chave]) # para que eu consiga acessar o valor tenho que colocar a variável que armazena o dicionário  e entre colchetes colocar qual a chave do momento da iteração

print()

for chave, valor in contatos.items():
    print(chave, valor)

