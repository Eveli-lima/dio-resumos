# OPERADORES LÓGICOS

'''SÃO USADOS EM CONJUNTO COM OPERADORES DE COMPARAÇÃO, PARA MONTAR UMA EXPRESSÃO LÓGICA. O RESULTADO RETORNADO É BOOLEANO, ASSIM PODEMOS COMBINAR OPERADORES DE COMPARAÃO COM OS OPERADORES LÓGICOS, EX.: OP_COMP. + OP_LOGICO _ OP_COMP...N...'''
print("===================")
# AND = PARA SER TRUE TUDO TEM QUE SER TRUE
print(True and True)
print(True and False)
print(False and False)

# OR = PARA SER TRUE APENAS UM TEM QUE SER TRUE
print(True or True)
print(True or False)
print(False or False)

print("===================")

saldo = 1000
saque = 200
limite = 100

# OPERADOR E (AND)

exp = saldo >= saque and saldo <= limite # False
'''     TRUE    |  FALSE   |    FALSO   '''
'''     TRUE    |  TRUE    |    TRUE   '''
print("1:", exp)
# OPERADOR OU (OR) 

exp2 = saldo >= saque or saldo <= limite # True
'''     TRUE    |  TRUE    |    TRUE   '''
'''     TRUE    |  FALSE   |    TRUE   '''
'''     FALSE   |  TRUE    |    TRUE   '''
'''     FALSE   |  FALSE   |    FALSE  '''
print("2:", exp2)
# OPERADOR DE NEGAÇÃO NÃO (NOT)

contatos_emergencia = []

not 1000 > 1500 # True

not contatos_emergencia # True
'''posso negar valores dentro de uma sequência, uma lista é uma sequência, string também é uma sequência, a lista é uma sequência de objetos e a string é uma seência de caractéres. Uma sequência vazia é considerado falso, então uma lista [] sem elementos é considerado falso e uma string vazia "" é considerado falso.'''

not "saque 1500;" # False

not "" # True

# PARÊNTESES

saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp3 = saldo >= saque and saque <= limite or conta_especial and saldo >= saque # True
print("3:", exp3)
exp4 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque) # True
print("4:", exp4)

'''NÃO FAZER UMA EXPRESSÃO LÓGICA MUITO GRANDE O IDEAL É QUEBRAR E DIVIDIR FAZENDO NOVAS ATRIBUIÇÕES. POR EXEMPLO A EXPRESSÃO ABAIXO DEIXA O CÓDIGO MAIS LEGIVEL'''

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

exp5 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente

print("5:", exp5)