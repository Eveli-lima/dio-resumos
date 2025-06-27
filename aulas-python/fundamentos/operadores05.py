# OPERADORES DE IDENTIDADE
'''UTILIZADOS PARA COMPARAR SE DOIS OBJETOS TESTADOS OCUPAM A MESMA POSIÇÃO NA MEMÓRIA'''

curso = "Curdo de Python"
nome_curso = cursosaldo, limite = 200, 200

curso is nome_curso # is é o operador de identidade, resultado: True
'''Qando eu quero comparar se o objeto a ocupa a mesma região de memória que o objeto b eu utilizo o is como na expressão acima. então curso recebe "Curso de Python" na memória, em seguida curso é atribuido a nome_curso que é "Curso de Python", ou seja, as duas variáveis ocupam o mesmo lugar na memória. o is verifica isso.'''

curso is not nome_curso # is not é a negação, resultado: False

'''saldo is limite''' # aqui mostra que não funciona apenas com strings mas com valores inteiros também, resultado: True

saldo = 1000
limite = 500

print(saldo is limite) # False
print(saldo is not limite) # True