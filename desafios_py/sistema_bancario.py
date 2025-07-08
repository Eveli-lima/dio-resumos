menu = f'''
    ============= Bem Vindo! ==============
    
    [1] DEPÓSITO
    [2] SAQUE
    [3] EXTRATO
    [0] SAIR

   ======================================== 
'''

saldo = 0
limite = 500
saques = 0
LIMITE_SAQUE = 3
extrato = ""

 
while True:

    try:
        opcao = int(input(menu))

        # DEPÓSITO
        if opcao == 1:
            entrada = float(input("Digite o valor do Depósito: ").replace(',', '.'))

            if entrada > 0:
                saldo += entrada
                extrato += f"Depósito: R$ {entrada:.2f}\n"
            else:
                print("Falha na operação! O valor deve ser maior que zero.")

        # SAQUE
        elif opcao == 2:
            saida = float(input("Digite o valor do saque: ").replace(',', '.'))

            excedeu_saldo = saida > saldo
            excedeu_limite = saida > limite
            excedeu_saques = saques >= LIMITE_SAQUE

            if excedeu_saldo:
                print("Operação falhou! VocÊ não tem saldo suficiente.")

            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")

            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")

            elif saida > 0:
                saldo -= saida
                extrato += f"Saque: R$ {saida:.2f}\n"
                saques += 1

            else:
                print("Falha na operação! O valor é inválido")    
        
        # EXTRATO
        elif opcao == 3:
            print("extrato".center(20, "=")) 
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}") 
            print("=".center(20, "="))   

        #SAIR
        elif opcao == 0:

            msn = f''' 
    ========= Obrigada, Volte sempre! =========

    Sistema Bancário v1.0 
    Desenvolvido por: Éveli Lima 
                '''
            print(msn)
            break
        else:
            print("O valor digitado não é válido. \nDigite um número de 0 a 3.")
    
    except ValueError:
        print("Falha na operação! O valor digitado não é um número válido. \nDigite um número de 0 a 3.")   

