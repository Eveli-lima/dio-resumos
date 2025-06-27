#ESTRUTURAS CONDICIONAIS

'''PERMITE O DESVIO DE FLUXO DE CONTROLE, QUANDO DETERMINADAS EXPRESSÕES LÓGICAS SÃO ATENDIDAS.'''

# IF - ESTRUTURA CONDICIONAL SIMPLES, COMPOSTA POR UM ÚNICO DESVIO, o COMANDO IF IRÁ TEXTAR A EXPRESSÃO LÓGICA, E EM CASO DE RETORNO VERDADEIRO AS AÇÕES PRESENTES DENTRO DO BLOCO SERÃO EXECUTADAS.

saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("realizando saque!...")

if saldo < saque:
    print("Saldo insuficiente!")


# IF/ELSE - ESTRUTURA CONDICIONAL COM DOIS DESVIOS, SE A EXPRESSÃO LÓGICA NO if FOR VERDADEIRA O BLOCO DO if SERÁ EXECUTADO. CASO CONTRÁRIO O BLOCO DE CÓDIGO DO ELSE SERÁ EXECUTADO.

saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("realizando saque!...")

else:
    print("Saldo insuficiente!")


# IF/ELIF/ELSE - EM ALGUNS CENÁRIOS QUEREMOS MAIS DE DOS DESVIOS, PARA ISSO USAMOS O elif. ELE PE COMPOSTO POR UMA NOVA EXPRESSÃO LÓGICA, QUE SERÁ TESTADA E CASO RETORNE VERDADEIRO O BLOCO DE CÓDIGO DO ELIF SERÁ EXECUTADO. NÃO EXISTE UM NUMERO MÁXIMO DE elifs QUE PODEMOS UTILIZAR, PORÉM EVITE CRIAR GRANDES ESTRUTURAS CONDICIONAIS, POIS ELAS AUMENTAM A COMPLEXIDADE DO CÓDIGO

opcao = int(input("[1] sacar \n[2] Extrato \nDigite uma opção: "))

if opcao== 1:
    valor = float(input("Informe a quantia para saque: "))

elif opcao == 2:
    print("Exibindo o extrato...")

else:
    print("Opção inválida")




