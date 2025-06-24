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

conta_normal = False
conta_universitária = False 
conta_especial = True

saldo = 2000
saque = 1500
cheque_especial = 600

print("============banco===========")
if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Não foi possível realizar o saque, saldo insuficiente!")

elif conta_universitária:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")

elif conta_especial:
    print("Conta especial selecionada!")
else:
    print("O sistema não reconhece sua conta, entre em contato com o banco.")

# IF TERNÁRIO

'''O IF TERNÁRIO PERMITE ESCREVER UMA CONDIÇÃO EM UMA UNICA LINHA. ELE É COMPOSTO POR TRÊS PARTES, A PRIMEIRA É O RETORNO CASO A EXPRESSÃO RETORNE VERDADEIRO, A SEGUNDA É A EXPRESSÃO LÓGICA E A TERCEIRA PARTE É O RETORNO CASO A EXPRESSÃO NÃO SEJA ATENDIDA.'''

status = "sucesso" if saldo >= saque else "falha"
print(f"{status} ao realizar o saque!")