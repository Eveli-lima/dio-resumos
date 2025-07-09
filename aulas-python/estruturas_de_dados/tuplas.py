# TUPLAS - CRIAÇÃO E ACESSO AOS DADOS 

'''SÃO ESTRUTURAS DE DADOS MUITO PARECIDAS COM AS LISTAS, A PRINCIPAL DIFERENÇA É QUE TUPLAS SÃO IMUTÁVEIS ENQUANTO LISTAS SÃO MUTÁVEIS. PODEMOS CRIAR TUPLAS ATRAVÉS DA CLASSSE TUPLE, OU COLOCANDO VALORES SEPARADOS POR VÍRGULAS E PARENTESES.'''

print()
print(" tuplas ".center(30, "="))

frutas = ("laranja", "pera", "uva",) # colocar uma vírgula no final da tupla indica ao python que se trata de uma tupla e não uma ordem de precedencia.
print(frutas)

letras = tuple("python")
print(letras)

numeros = tuple([1, 2, 3, 4])
print(numeros)

pais = ("Brasil",)
print(pais)

# ACESSO DIRETO

'''A TUPLA É UMA SEQUÊNCIA, PORTANTO PODEMOS ACESSAR SEUS DADOS UTILIZANDO ÍNDICES. CONTAMOS O ÍNDICE DE DETERMINADA SEQUÊNCIA A PARTIR DO ZERO.'''

print()
print(" Acesso direto ".center(30, "="))

frutas = ("maçã", "laranja", "uva", "pera",) 

print(frutas[0])
print(frutas[2])

# TUPLA ANINHADAS

'''TUPLAS PODEM ARMAZENAR TODOS OS TIPOS DE OBJETOS PYTHON, PORTANTO PODEMOS TER TUPLAS QUE ARMAZENAMM OUTRAS TUPLAS. COM ISSO PODEMOS CRIAR ESTRUTURAS BIDIMENCIONAIS (TABELAS), E ACESSAR INFORMANDO OS ÍNDICES DE LINHA E COLUNA'''

# Vou usar a tupla quando tenho certeza que algo não será alterado.

print()
print(" tuplas aninhadas ".center(30, "="))

matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c")
)

print(matriz[0])
print(matriz[0][0])        
print(matriz[0][-1])
print(matriz[-1][-1])

# FATIAMENTO

'''ALÉM DE USAR ELEMENTOS DIRETAMENTE, PODEMOS EXTRAIR UM CONJUNTO DE VALOES DE UMA SEQUÊNCIA. PARA ISSO VASTA PASSA O ÍNDICE INICIAL E/O FINAL PARA ACESSAR O CONJUNTO. PODEMOS AINDA INFORMAR QUANTAS POSIÇÕES O CURSOR DEVVE "PULAR" NO ACESSO.'''

# START STOP STEP

print()
print(" fatiamento ".center(30, "="))

tupla = ("p", "y", "t", "h", "o", "n",)

print(tupla[2:])
print(tupla[:2])
print(tupla[1:3])
print(tupla[0:3:2])
print(tupla[::])
print(tupla[::-1])

# iterar

print()
print(" Iterar ".center(30, "="))

"""A FORMA MAIS COMUM PARA PERCORRER OS DADOS DE UMA TUPLA É UTILIZANDO O COMANDO FOR."""

carros = ("gol", "celta", "palio",)

for carro in carros:
    print(carro)

# enumerate

"""ÀS VEZES É NECESSÁRIO SABER QUAL O ÍNDICE DO  OBJETO DENTRO DO LAÇO FOR. PARA ISSO PODEMOS USAR A FUNÇÃO ENUMERATE."""

print()
print(" enumerate ".center(30, "="))

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

