 # MÉTODOS DA CLASSE SET

# {}.union

print()
print(" .union ".center(30, "="))

conjunto_a = {1, 2}
conjunto_b = {3, 4}

print(conjunto_a.union(conjunto_b)) # une os dois conjuntos em um

# {}.intersection

print()
print(" .intersection ".center(30, "="))

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.intersection(conjunto_b)) # exibe a intecessão entre dois conjuntos

# {}.difference

print()
print(" .difference ".center(30, "="))

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.difference(conjunto_b)) # exibe o que tem apenas no conjunto_a e não tem no conjunto_b
print(conjunto_b.difference(conjunto_a)) # exibe o que tem apenas no conjunto_b e não tem no conjunto_a

# {}.symmetric_difference

print()
print(" .symmetric_difference ".center(30, "="))

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.symmetric_difference(conjunto_b)) # exibe todos os elementos menos a intersessão

# {}.issubset

print()
print(" .issubset ".center(30, "="))

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

print(conjunto_a.issubset(conjunto_b)) # exibe True
print(conjunto_b.issubset(conjunto_a)) # exibe False
# verifica se um conjunto contém em outro conjunto.

# {}.issuperset

print()
print(" .issuperset ".center(30, "="))

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

print(conjunto_b.issuperset(conjunto_a)) # exibe False
print(conjunto_a.issuperset(conjunto_b)) # exibe True
# é o contrário de {}.issubset

# {}.isdisjoint

print()
print(" .isdisjoint ".center(30, "="))

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

print(conjunto_a.isdisjoint(conjunto_b)) # True
print(conjunto_a.isdisjoint(conjunto_c)) # False
# verifica se são conjuntos disjuntos, separados.

# {}.add

print()
print(" .add ".center(30, "="))

sorteio = {1, 23}
print(sorteio)

sorteio.add(25) # será adicionado no conjunto
print(sorteio)

sorteio.add(42)
print(sorteio)

sorteio.add(25) # se eu repetir o mesmo objeto será ignorado
print(sorteio)

# {}.clear

print()
print(" .clear ".center(30, "="))

sorteio = {1, 23}
print(sorteio)

sorteio.clear() # vai deixar o conjunto vazio
print(sorteio)

# {}.copy

print()
print(" .copy ".center(30, "="))

sorteio = {1, 23}
print(sorteio)

sorteio.copy() # vai fazer uma cópia identica do conjunto
print(sorteio)

# {}.discard

print()
print(" .discard ".center(30, "="))

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print(numeros) # exibe os números em ordem e sem os numeros duplicados

numeros.discard(1) # vai descartar o valor 1
print(numeros)
numeros.discard(45) # 45 não existe nesse método então não acontece nada
print(numeros)

# {}.pop

print()
print(" .pop ".center(30, "="))

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print(numeros) # exibe os números em ordem e sem os numeros duplicados

numeros.pop() # por padrão vai tirando os primeiros números que encontrar 
print(numeros)
numeros.pop() 
print(numeros)
numeros.pop() 
print(numeros)
numeros.pop() 
print(numeros)
numeros.pop() 
print(numeros)
numeros.pop() 
print(numeros)
numeros.pop() 
print(numeros)

print()
print(" .pop2 ".center(30, "="))

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print(numeros) # exibe os números em ordem e sem os numeros duplicados

print(numeros.pop())
print(numeros.pop())
print(numeros.pop())
print(numeros.pop())
print(numeros.pop())
print(numeros.pop())
print(numeros.pop())
print(numeros.pop())
print(numeros.pop())

# {}.remove

print()
print(" .remove ".center(30, "="))

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print(numeros) # exibe os números em ordem e sem os numeros duplicados

numeros.remove(0) # remove o elemento
print(numeros)
# é parecido com o discard. a diferença é que se o elemento não existe ele exibe um erro. no discard não acontece nada

# len()

print()
print(" len() ".center(30, "="))

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print(numeros) # exibe os números em ordem e sem os numeros duplicados
 
print(len(numeros)) # exibe o tamanho do conjunto

# in

print()
print(" in ".center(30, "="))

print(1 in numeros)
print(10 in numeros)
#verifica se um elemento está no conjunto



#produto = {
#    "nome_do_produto" : "Champoo",
#    "preço" : 35,
#    "quantidade_em_estoque" : 10
#
#}
#
#total = produto["preço"] * produto["quantidade_em_estoque"]
#
#print()
#print(" xxx ".center(20, "="))
#print()
#
#print("Nome do produto:", produto["nome_do_produto"])
#print("Preço: R$ ", float(produto["preço"]))
#print("Quantidade em estoque:", produto["quantidade_em_estoque"])
#print()
#print("Valor total do estoque:", total)
#
#print()
#print(" xxx ".center(20, "="))

#===================================

#nomes = ["joão", "maria", "josé", "judas"]
#
#for indice, nome in enumerate(nomes[1:3], start=1):
#    print(f"{indice}: {nome}")

#===================================


    


