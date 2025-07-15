# DICIONÁRIO - MÉTODOS DA CLASSE DICT

# {}.clear

print()
print(" .clear ".center(30, "="))

contatos = {
    "eveliazevedo@gmail.com": {'nome': 'Éveli', 'telefone': '(21) 9999-9999'},
    "fulana@gmail.com": {'nome': 'Fulana', 'telefone': '(21) 2222-2222'},
    "beutrana@gmail.com": {'nome': 'Beutrana', 'telefone': '(21) 3333-3333'},
    "cicrana@gmail.com": {'nome': 'Cicrana', 'telefone': '(21) 5555-5555'},
}

print()
print(contatos)
print()

contatos.clear()
print("Limpa tudo:", contatos)

# {}.copy

"""TIRA UMA CÓPIA DOS DICIONÁRIOS.
PORÉM AO SER MODIFICADO ELE NÃO
INTERFERE NO DICIONÁRIO ORIGINAL"""

print()
print(" .copy ".center(30, "="))

contatos = {
    "eveliazevedo@gmail.com": {'nome': 'Éveli', 'telefone': '(21) 9999-9999'}
}

copia = contatos.copy() #crio uma cópia
copia["eveliazevedo@gmail.com"] = {"nome": "Vela"} #altero o valor relacionado com a chave

print(contatos["eveliazevedo@gmail.com"])
print(copia["eveliazevedo@gmail.com"]) # vc altera o dicionário sem alterar o dicionário original

# {}.fromkeys

# cria chaves e não adiciona nenhum valor

print()
print(" .fromkeys ".center(30, "="))

a = dict.fromkeys(["nome", "telefone"])
print(a)

b = dict.fromkeys(["nome", "telefone"], "vazio")
print(b)
#se for um dicionário existente coloca o nome do dicionário no lugar do dict

# {}.get

# usamos para saber se uma chave existe ou não

print()
print(" .get ".center(30, "="))

contatos = {
    "eveliazevedo@gmail.com": {'nome': 'Éveli', 'telefone': '(21) 9999-9999'}
}

print(contatos.get("chave", {}))
print(contatos.get("eveliazevedo@gmail.com", {}))
# encontre essa chave, se não encontrar me devolva um elemento vazio, isso evita dar erro caso não tenha a chave no dicionário


# {}.items

# retorna uma lista de tuplas, é mt útil quando eu fizer um comando for para iterar sobre os valores do dicionário

print()
print(" .items ".center(30, "="))

contatos = {
    "eveliazevedo@gmail.com": {'nome': 'Éveli', 'telefone': '(21) 9999-9999'}
}

print(contatos.items())

# {}.keys

print()
print(" .keys ".center(30, "="))

print("Retorna só as chaves do dicionário")
print(contatos.keys())

# {}.pop

print()
print(" .pop ".center(30, "="))

contatos = {
    "eveliazevedo@gmail.com": {'nome': 'Éveli', 'telefone': '(21) 9999-9999'}
}
print(contatos)
print() 

print("vai remover uma chave do dicionário")
print() 

print(contatos.pop("eveliazevedo@gmail.com"))
print(contatos.pop("eveliazevedo@gmail.com", {}))


# {}.popitem

"""VAI RETIRANDO OS ITENS NA SEQUENCIA"""

print()
print(" .popitem ".center(30, "="))

contatos = {
    "eveliazevedo@gmail.com": {'nome': 'Éveli', 'telefone': '(21) 9999-9999'},
    "fulana@gmail.com": {'nome': 'Fulana', 'telefone': '(21) 2222-2222'}
}
print(contatos)


print()

print(contatos.popitem())


# {}.setdefault
 
# Se o valor não estiver no dicionário ele adiciona o que eu indicar, se o valor tiver no dicionário ele não é alterado.

print()
print(" .setdefault ".center(30, "="))

contatos = {'nome': 'Éveli', 'telefone': '(21) 9999-9999'}

print(contatos)
print()

contatos.setdefault("nome", "Lima")
print(contatos)
print()

contatos.setdefault("idade", 37)
print(contatos)


# {}.update
"""PERMITE ATUALIZAR O NOSSO DICIONÁRIO COM OUTRO DICIONÁRIO"""

print()
print(" .update ".center(30, "="))

contatos = {
    "eveliazevedo@gmail.com": {'nome': 'Éveli', 'telefone': '(21) 9999-9999'},
}

print(contatos)
print()

contatos.update({"eveliazevedo@gmail.com": {"nome": "Vela"}}) #se a chave existir ele atualiza as informações escrendo por cima 
print(contatos)
print()

contatos.update({"fulana@gmail.com": {'nome': 'Fulana', 'telefone': '(21) 2222-2222'}}) #se a chave não existir ele vai incluir no dicionário
print(contatos)


# {}.values

"""O keys retorna todas as chaves do dicionário, mas temos o método que retona só os valores que é o caso do .values, é muito útil tbm quando vc não precisa saber as chaves, quando precisa iterar apenas sobre os valores"""

print()
print(" .values ".center(30, "="))

contatos = {
    "eveliazevedo@gmail.com": {'nome': 'Éveli', 'telefone': '(21) 9999-9999'},
    "fulana@gmail.com": {'nome': 'Fulana', 'telefone': '(21) 2222-2222'},
    "beutrana@gmail.com": {'nome': 'Beutrana', 'telefone': '(21) 3333-3333'},
    "cicrana@gmail.com": {'nome': 'Cicrana', 'telefone': '(21) 5555-5555', "extra": {"a": 1}},
}

print(contatos.values())

# {}.in

"""É UMA FORMA ELEGANTE PARA SABER SE UMA CHAVE EXISTE OU NÃO NO DICIONÁRIO"""

print()
print(" .in ".center(30, "="))

print("eveliazevedo@gmail.com" in contatos)
print("patatipata@gmail.com" in contatos)
print("idade" in contatos["eveliazevedo@gmail.com"])
print("telefone" in contatos["cicrana@gmail.com"])

# {}.del

"""è uma outra forma de tirar um valor do dicionário ou toda a chave"""

print()
print(" .del ".center(30, "="))

del contatos["eveliazevedo@gmail.com"]["telefone"]
del contatos["cicrana@gmail.com"]

print(contatos)