# ESTRUTURAS CONDICIONAIS - PRÁTICAS 

MAIOR_IDADE = 18
IDADE_ESPECIAL = [16, 17,]


print("=============if==================")

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade pode tirar a CNH.")

if idade < MAIOR_IDADE:
    print("Menor de idade não pode tirar a CNH.")

print("=============else==================")

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade pode tirar a CNH.")

else: 
    print("Menor de idade não pode tirar a CNH.")

print("=============elif==================")

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade pode tirar a CNH.")

elif idade in IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, Mas não pode fazer aulas práticas.")

else: 
    print("Menor de idade não pode tirar a CNH.")

# IF ANINHADO

'''PODEMOS CRIAR ESTRUTURAS CONSICIONAIS ANINHADAS, BAASTA ADICIONAR ESTRUTURAS if/elif/else DENTRO DO BLOCO DE CÓDIGO DE ESTRUTURAS if/elif/else.'''

conta_normal = 300
conta_universitária = 500
saldo = conta_normal + conta_universitária
saque = int(input("Qual o valor do saque?: "))

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
elif conta_universitária:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")