# CONJUNTOS - CRIANDO SETS

'''UM SET É UMA COLEÇÃO QUE NÃO POSSUI OBJETOS REPETIDOS, USAMOS SETS PARA REPRESENTAR CONJUNTOS MATEMÁTICOS OU ELIMINAR ITEN DUPLICADOS DE UM ITERÁVEL.'''

# NÃO TEM ITENS DUPLICADOS

print()
print(" conjuntos ".center(30, "="))

print(set([1, 2, 3, 1, 3, 4]))

print(set("abacaxi")) # não vai ficar em ordem

print(set(("palio", "gol", "celta", "palio",)))

# POSSO USAR PARÊNTESES OU CHAVES, SE EU USAR PARENTESES TENHO QUE COLOCAR O SET ANTES.

linguagem = {"python", "java", "python"}
print(linguagem)

# ACESSANDO OS DADOS

'''CONJUNTOS NÃO SUPORTAM INDEXAÇÃO E NEM FATIAMENTO, CASO QUEIRA ACESSAR OS SEUS VALORES É NECESSÁRIO CONVERTER O CONJUNTO PARA LISTA.'''

print()
print(" acessando os dados ".center(30, "="))

numeros = {1, 2, 3, 2}

numeros = list(numeros)

print(numeros[0])

# ITERAR CONJUNTOS

'''A FORMA MAIS COMUM PARA PERCORRER OS DADOS DE UM CONJUNTO É UTILIZANDO O COMANDO FOR'''

print()
print(" iterar ".center(30, "="))

carros = {"gol", "celta", "palio"}

for carro in carros:
    print(carro)

# FUNÇÃO ENUMERATE

'''AS VEZES É NECESSÁRIO SABER QUAL O ÍNDICE DO OBJETO DENTRO DO LAÇO FOR. PARA ISSO PODEMOS USAR A FUNÇÃO ENUMERATE'''

print()
print(" função enumerate ".center(30, "="))

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")









