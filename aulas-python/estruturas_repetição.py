# ESTRUTURAS DE REPETIÇÃO

'''SÃO ESTRUTURAS UTILIZADAS PARA REPETIR UM TRECHO DE CÓDIGO UM DETERMINADO NÚMERO DE VEZES. ESSE NÚMERO PODE SER CONHECIDO PREVIAMENTE OU DETERMINADO ATRAVÉS DE UMA EXPRESSÃO LÓGICA.'''

# Receba um número do teclado e exiba os 2 números seguintes

'''
EXEMPLO:

a = int(input("informe um número inteiro: "))

a += 1 
print(a)

a += 1
print(a)

repita 2 vezes:
    a += 1
    print(a)
'''

# COMANDO FOR

'''O COMANDO for É USADO PARA PERCORRER UM OBJETO ITERÁVEL. FAZ SENTIDO USAR for QUANDO SABEMOS O NÚMERO EXATO DE VEZES QUE NOSSO BLOCO DE CÓDIGO DEVE SER EXECUTADO, OU QUANDO QUEREMOS PERCORRER UM OBJETO ITERÁVEL'''

texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

print() # adiciona uma quebra de linha

'''Uma string em python é um objeto iterával, o for percorre item a item, letra por letra
o for tem duas partes o objeto iterável que eu quero percorrer e a segunda parte é o item que está sendo iterado naquele momento.

'''

# FOR/ELSE

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

else:
    print() # adiciona uma quebra de linha
    print("Executa no final do laço.")

#Nesse caso de usar o else com o for não é mt comum no dia a dia.

# FUNÇÃO RANGE

'''RANGE É A FUNÇÃO BUILT-IN DO PYTON, ELA É USADA PARA PRODUZIR UMA SEQUÊNCIA DE NÚMEROS INTEIROS A PARTIR DE UM INÍCIO (INCLUSIVO) PARA UM FIM (EXCLUSIVO) (isso quer dizer, por exemplo, se eu colocar de 0 a 10 ele vai incluir o número zero pq é o início pq ele é inclusivo e o 10 vai ficar de fora pq ele é exclusivo no fim, então vai gerar de 0 a 9). SE USARMOS RANGE(i, j) SERÁ PRODUZIDO:

i, i+1, i+2, i+3, ..., j-1.

ELA RECEBE 3 ARGUMENTOS: STOP (OBRIGATÓRIO), START (OPCIONAL) E STEP OPCIONAL.
'''

# range(stop) -> range object
# range(start, stop[, step]) -> range object
#(START=INICIO, STOP=FIM, STEP=ETAPA/PASSO/DEGRAU)
print()
print(range(4)) #>>> (0, 4)
print(list(range(4))) #>>> [0, 1, 2, 3]

print()
print("**********************************")

for numero in range(0, 11): # O 11 É EXCLUSIVO ENTÃO TERMINA EM 10
    print(numero, end=" ")
#>>> 0 1 2 3 4 5 6 7 8 9 10

print()
print("**********************************")

# TABUADA DE 5
print("Tabuada de 5")
for numero in range(0, 51, 5): # de 0 a 51 pulando de 5 em 5. (INICIO, FIM, ETAPA/PASSO/DEGRAU)
    print(numero, end=" ")
#>>> 0 5 10 15 20 25 30 35 40 45 50
print()
print("**********************************")

# COMANDO WHILE (while)

'''É USADO PARA REPETIR UM BLOCO DE CÓDIGO VÁRIAS VEZES. FAZ SENTIDO USAR O WHILE QUANDO NÃO SABEMOS O NÚMERO EXATO DE VEZES QUE NOSSO BLOCO DE CÓDIGO DEVE SER EXECUTADO.'''

opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2]Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando ...")
    elif opcao == 2:
        print("Exibindo extrato ...")
else: # else com while assim como o for não é mt utilizado

    print("Saindo ...")

print("*************para se digitar 10**********************")

#looping infinito com uma estrutura de condição que interrompe o looping.
while True:
    numero = int(input("Digite um número: "))
    if numero == 10:
        break
    print(numero)

print("**************para no 12*********************")

for number in range(100):
    if number == 12: 
        break  # exibe de 0 a 11 
    print(number, end=" ")

print()
print("*************elimina o 12**********************")

for number in range(100):
    if number == 12:
        continue    #exibe de 0 a 99 e pula o 12
    print(number, end=" ")

print()
print("*************n° ímpares**********************")

for number in range(100):
    if number % 2 == 0:
        continue    #exibe de 0 a 99 e pula o 12
    print(number, end=" ")
 
 '''O BREAK VAI PARAR A EXECUÇÃO E O CONTINUE VAI PULAR A CONDIÇÃO E CONTINUAR A EXECUÇÃO.
 POSSO USAR O CONTINUE DENTRO DO while
 '''