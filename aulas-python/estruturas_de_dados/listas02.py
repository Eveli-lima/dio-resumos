# Método da classe list

# [].append

print()
print(" .append ".center(30, "="))

lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20]) # acrescenta à lista

print(lista)

# [].clear

print()
print(" .clear ".center(30, "="))

lista.clear() # esvazia a lista

print(lista)

# [].copy

print()
print(" .copy ".center(30, "="))

l1 = [1, 'Python', [40, 30, 20]]

print(l1)
print(id(l1))

l2 = l1.copy() # vai retornar uma lista igual poré com uma instancia diferênte, ou seja, não é a mesma lista.

print(l2)
print(id(l2))
# o que eu fizer no l2 não vai interferir no l1 pois eles tem ids diferentes

l2[0] = 2

print(l1)
print(l2)

# Assim eu garanto que tenho uma lista com o mesmo valor onde eu posso editar sem alterar a lista original

# [].count

print()
print(" .count ".center(30, "="))

cores = ["vermelho", "azul", "verde", "azul"]

print(cores.count("vermelho"))
print(cores.count("azul"))
print(cores.count("verde")) # serve para contar quantas vezes um objeto aparece dentro da lista

# [].extend
# é muito utilizado! 

print()
print(" .extend ".center(30, "="))

linguagem = ["python", "js", "c"]

print("liata 01:", linguagem)

linguagem.extend(["java", "csharp", "c"]) # junta uma lista na outra, e ele repete os objetos que forem iguais nas duas listas.

print("liata 02:", linguagem)

# [].index

print()
print(" .index ".center(30, "="))

linguagem = ['python', 'js', 'c', 'java', 'csharp']

print(linguagem.index("java")) # qual é a posição do objeto posição 0 1 2 ou 3 ...
print(linguagem.index("python"))

# o index não vai retornar todas as oocorrências, mas vai retornar a primeira ocorrência do objeto

# para pegar todas as ocorrencias de um objeto precisa fazer uma combinação com o .count

# [].pop
''' a lista por padrão ja vem organizada como uma pilha. o primeiro elemento fica embaixo o segundo elemento em cima e assim por diante. o programa pega o elemento qie está em cima pois foi o último que foi adicionado, ou seja, que está em cima da pilha'''

'''O .append adiciona um item no fim da lista. quando utilizamos o pop do jeito padrão ele tira o elemento do fim da lista'''


print()
print(" .pop ".center(30, "="))

print(linguagem.pop())
print(linguagem.pop())
print(linguagem.pop())
print(linguagem.pop(0)) # eu posso passar qual o elemento que eu quero remover


# [].remove

print()
print(" .remove ".center(30, "="))

linguagens = ['python', 'js', 'c', 'java', 'csharp']

print(linguagens)

linguagens.remove("c")

print(linguagens)

# se eu tiver mais de uma ocorrencia de C ele cai tirar apenaas a primeira que ele encontear na ordem da lista. para remover todas as ocorrências pode fazer uma lógica de usar o .count para saber quantas ocorrências tem e depois remover.

# [].reverse

print()
print(" .reverse ".center(30, "="))

linguagens.reverse() # espelha a lista, é como se colocasse ao contrário

print(linguagens)

# [].sort

print()
print(" .sort ".center(30, "="))

linguagens1 = ['python', 'js', 'c', 'java', 'csharp']
print(linguagens1)
print()

linguagens1.sort() # vai ordenar alfabéticamente a lista
print(linguagens1," - ordem alfabética")

linguagens1.sort(reverse=True)
print(linguagens1," - ordem alfabética e contrária")

linguagens1.sort(key=lambda x: len(x)) # o lambda é uma função sem nome e o x é o argumento, que é cada item da lista, então o x vai ser igual a python depois igual a js e assim por diante. o len mostra quantos caracteres tem no objeto na lista
print(linguagens1," - ordem por tamanho crescente")

linguagens1.sort(key=lambda x: len(x), reverse=True)
print(linguagens1," - ordem por tamanho crescente e contrária")

# [].len

# é uma função builtin

print()
print(" .len ".center(30, "="))

print(len(linguagens1)) # retorna o número de caracteres

# [].sorted

# é uma função builtin e serve tambem para ordenar iteráveis. a diferença do sorte é que ele é uma função

print()
print(" .sorted ".center(30, "="))

linguagem = ['python', 'js', 'c', 'java', 'csharp']

print(sorted(linguagem, key=lambda x: len(x)))

print(sorted(linguagem, key=lambda x: len(x), reverse=True))



numeros = [n**2 if n > 6 else n for n in range(10) if n % 2 == 0] 
print(numeros)


