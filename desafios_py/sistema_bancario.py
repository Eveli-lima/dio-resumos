from datetime import datetime

def menu_principal():
    print("""
    ============= BEM VINDO! ==============

    [1] ACESSAR CONTA
    [2] CADASTRAR CLIENTE
    [3] ABRIR CONTA CORRENTE
    [0] SAIR

    ========================================
    """)

def menu_conta_corrente(usuario, conta, saques_realizados, LIMITE_SAQUE_DIARIO):
    agora = datetime.now()
    data= agora.strftime("%d/%m/%Y")
    hora = agora.strftime("%H:%M")

    limite_restante = LIMITE_SAQUE_DIARIO - saques_realizados

    print(f"""
    ============= Conta de {usuario['nome']} ==============
    Agência: {conta['agencia']}                           conta:{conta['numero']}

    [1] DEPÓSITO
    [2] SAQUE
    [3] EXTRATO
    [4] LISTAR CONTAS
    [0] SAIR

    Limite de saques restante: {limite_restante}
    ===============================================
    DATA: {data}                    HORA: {hora}
    """)

def buscar_usuario_por_cpf(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None

def cadastrar_usuario(usuarios):
    cpf = input("Digite o CPF (somente números): ")
    usuario_existente = any(usuario["cpf"] == cpf for usuario in usuarios)

    if usuario_existente:
        print("Já existe usuário com esse CPF!")
        return

    nome = input("Digite o nome completo: ")
    nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Digite o endereço (logradouro, número - bairro - cidade/UF): ")

    usuario = {
        "nome": nome,
        "data_nascimento": nascimento,
        "cpf": cpf,
        "endereco": endereco
    }

    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")

def criar_conta(usuarios, contas):
    cpf = input("Digite o CPF do titular da conta: ")
    usuario = buscar_usuario_por_cpf(cpf, usuarios)

    if usuario:
        conta = {
            "agencia": "0001",
            "numero": len(contas) + 1,
            "usuario": cpf
        }
        contas.append(conta)
        print("Conta criada com sucesso!")
    else:
        print("Usuário não encontrado! Cadastre o cliente antes de criar a conta.")

def listar_contas(cpf, contas):
    contas_do_usuario = [conta for conta in contas if conta["usuario"] == cpf]

    if not contas_do_usuario:
        print("Esse usuário não possui contas cadastradas.")
        return

    print("\n=== LISTA DE CONTAS DO USUÁRIO ===")
    for conta in contas_do_usuario:
        usuario = buscar_usuario_por_cpf(cpf, usuarios)
        nome = usuario["nome"] if usuario else "Desconhecido"
        print(f"Agência: {conta['agencia']} | Conta: {conta['numero']} | Titular: {nome} (CPF: {cpf})")
    print("===================================")


def acessar_conta(usuarios, contas):
    cpf = input("Digite o CPF do titular da conta: ")
    usuario = buscar_usuario_por_cpf(cpf, usuarios)

    if not usuario:
        print("Usuário não encontrado!")
        return

    contas_do_usuario = [conta for conta in contas if conta["usuario"] == cpf]

    if not contas_do_usuario:
        print("Nenhuma conta encontrada para esse usuário.")
        return

    print("\n=== CONTAS ENCONTRADAS ===")
    for i, conta in enumerate(contas_do_usuario, start=1):
        print(f"[{i}] Agência: {conta['agencia']} | Conta: {conta['numero']}")
    print("===========================")

    if cpf not in saques_por_cpf:
        saques_por_cpf[cpf] = 0

    try:
        escolha = int(input("Digite o número da conta que deseja acessar: "))
        conta = contas_do_usuario[escolha - 1]
    except (ValueError, IndexError):
        print("Opção inválida.")
        return

    saldo = 0
    limite = 500
    saques_realizados = saques_por_cpf[cpf]
    LIMITE_SAQUE = 3
    historico = []

    while True:
        menu_conta_corrente(usuario, conta, saques_realizados,LIMITE_SAQUE)
        opcao = input()

        if opcao == "1":
            valor = float(input("Digite o valor do depósito: "))
            if valor > 0:
                saldo += valor
                historico.append(f"Depósito: R$ {valor:.2f}")
            else:
                print("Valor inválido!")

        elif opcao == "2":
            valor = float(input("Digite o valor do saque: "))
            if valor <= 0:
                print("Valor inválido!")
            elif valor > saldo:
                print("Saldo insuficiente!")
            elif valor > limite:
                print("Valor excede o limite por saque!")
            elif saques_realizados >= LIMITE_SAQUE:
                print("Número máximo de saques atingido!")
            else:
                saldo -= valor
                historico.append(f"Saque: R$ {valor:.2f}")
                saques_realizados += 1
                saques_por_cpf[cpf] = saques_realizados

        elif opcao == "3":
            print("\n======= EXTRATO =======")
            print(f"Cliente: {usuario['nome']}")
            print()
            if not historico:
                print("Nenhuma movimentação.")
            else:
                for operacao in historico:
                    print(operacao)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("======================")

        elif opcao == "4":
            listar_contas(cpf, contas)

        elif opcao == "0":
            print("Saindo da conta...\n")
            break

        else:
            print("Opção inválida!")

# Lista de dados
usuarios = []
contas = []
saques_por_cpf = {}

# Programa principal
while True:
    menu_principal()
    opcao = input()

    if opcao == "1":
        acessar_conta(usuarios, contas)
    elif opcao == "2":
        cadastrar_usuario(usuarios)
    elif opcao == "3":
        criar_conta(usuarios, contas)
    elif opcao == "0":
        print("Encerrando o sistema... Até logo!")
        break
    else:
        print("Opção inválida! Tente novamente.")
