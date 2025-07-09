# LISTAS

'''PODEM ARMAZENAR DE MANEIRA SEQUENCIAL QUALQUER TIPO DE OBJETO. UTILIZAMOS list, A FUNÇÃO range OU COLOCANDO OS VALORES SEPARADOS POR VIRGULA DENTRO DE COLCHETES PARA DECLARAR AS LISTAS. SÃO OBJETOS MUTÁVEIS.'''

print()
print(" listas ".center(30, "="))

frutas =["laranja", "maçã", "uva"]
print(frutas)

frutas = []
print(frutas)

letras = list("python")
print(letras)

numeros = list(range(10))
print(numeros)

carro = ["ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
print(carro)

#==========================================

# ACESSO DIRETO

'''LISTA É UMA SEQUÊNCIA, PORTANTO PODEMOS ACESSAR SEUS DADOS UTILIZANDO ÍNDICES. CONTAMOS O ÍNDICE DE DETERMINADA SEQUÊNCIA A PARTIR DO ZERO.'''

print()
print(" acesso direto ".center(30, "="))

frutas = ["maçã", "laranja", "uva", "pêra"]
print(frutas[0])
print(frutas[2])

#==========================================

# ÍNDICES NEGATIVOS

'''SEQUÊNCIAS SUPORTAM INDEXAÇÃO NEGATIVA. A CONTAGEM COMEÇA EM -1.'''

print()
print(" índices negativos ".center(30, "="))

frutas = ["maçã", "laranja", "uva", "pêra"]
print(frutas[-1])
print(frutas[-3])

#==========================================

# LISTAS ANINHADAS

'''LISTAS PODEM ARMAZENAR TODOS OS TIPOS DE OBJETOS PYTHON, PORTANTO PODEMOS TER LISTAS QUE ARMAZENAM OUTRAS LISTAS. COM ISSO PODEMOS CRIAR ESTRUTURAS BIDIMENSIONAIS (TABELAS), E ACESSAR INFORMANDO OS ÍNDICES DE LINHA E COLUNA.'''

print()
print(" matrizes ".center(30, "="))

matriz = [ 
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]
print(matriz[0]) # linha
print(matriz[0][0]) # linha e coluna
print(matriz[0][-1])
print(matriz[-1][-1])

#=========================================

# FATIAMENTO

'''ALÉM DE ACESSAR ELEMENTOS DIRETAMENTE, PODEMOS EXTRAIR UM CONJUNTO DE VALORES DE UMA SEQUÊNCIA. PARA ISSO BASTA PASSAR O ÍNDICE INICIAL E /OU FINAL PARA ACESSAR O CONJUNTO. PODEMOS AINDA INFORMAR QUANTAS POSIÇÕES O CURSOR DEVE "PULAR" NO ACESSO.'''

print()
print(" fatiamento ".center(30, "="))

lista = ["p", "y", "t", "h", "o", "n"]

# É obrigatório passar o início e o final, há uma excessão.
print(lista[2:]) # dois, dois pontos, e vazio significa até o final.
print(lista[:2]) # vazio, dois pontos, dois. nesse caso vai da posição zero até o ponto de parada que eu informar.
print(lista[1:3]) # inicial e final
print(lista[0:3:2]) # inicial e final pulando de 2 em 2
print(lista[::]) # do começo ao final. Esse é o caso da esseção pois não é infoemado o inicio nem o fim nem o passo.
print(lista[::-1]) # do final ao começo.

#==========================================

#  ITERAR LISTAS

'''a FORMA MAIS COMUM PARA PERCORRER OS DADOS DE UMA LISTA É UTILIZANDO O COMANDO FOR'''

print()
print(" iterar ".center(30, "="))

carros = ["gol", "celta", "palio"]

for carro in carros: # carro é uma variável criada que armazena os valores que foram verificados na lista 
    print(carro)

#==========================================

# FUNÇÃO ENUMERATE

'''AS VEZES É NECESSÁRIO SABER QUAL O ÍNDICE DO OBJETO DENTRO DO LAÇO FOR. PARA ISSO PODEMOS USAR A FUNÇAO ENUMERATE.'''

print()
print(" enumerate ".center(30, "="))

carros = ["gol", "celta", "palio"]

for indice, carro in enumerate(carros): # nesse caso ele me passa dois valores, um contador que começa em zero e o outro é o ítem da iteração
    print(f"{indice}: {carro}")

#=========================================

# COMPREENÇÃO DE LISTAS

'''OFERECE UMA SINTAXE MAIS CURTA QUANDO VOCÊ DESEJA: CRIAR UMA NOVA LISTA COM BASE NOS VALORES DE UMA LISTA EXISTENTE (FILTRO) OU GERAR UMA NOVA LISTA APLICANDO ALGUMAS MODIFICAÇÕES NOS ELEMENTOS DE UMA LISTA EXISTENTE'''


print()
print(" compreensão ".center(30, "="))

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros: # esse é uma forma de fazer em bloco
    if numero % 2 == 0:
        pares.append(numero)

print("bloco:", pares)

pares = [numero for numero in numeros if numero % 2 == 0] # o método compreensão simplofica escrevendo em linhas ao invés de escrever em blocos.

print("linha:", pares)

#============================================

# MODIFICANDO OS VALORES

print()
print(" modificando ".center(30, "="))

quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)

print("elevado ao quadrado:\nbloco", quadrado)

quadrado = [numero ** 2 for numero in numeros]
print("linha", quadrado)




