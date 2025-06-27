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

print()
print(" .copy ".center(30, "="))

print("tira uma cópia dos dicionários. \nPorém ao ser modificado ele não \ninterfere no dicionário original")

# {}.fromkeys

# cria chaves e não adiciona nenum valor

print()
print(" .fromkeys ".center(30, "="))

a = dict.fromkeys(["nome", "telefone"])
print(a)

b = dict.fromkeys(["nome", "telefone"], "vazio")
print(b)

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

# retorna uma lista de tuplas
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

print()
print(" .popitem ".center(30, "="))

print("vai retirando os itens na sequência")

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








# {}.copy

print()
print(" .copy ".center(30, "="))

# {}.copy

print()
print(" .copy ".center(30, "="))







