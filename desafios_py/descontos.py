descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = float(input("").strip())
cupom = input("").upper().strip()

if cupom in descontos:
    percentual = descontos[cupom]
    valor_do_desconto = percentual * preco
    preco_final = preco - valor_do_desconto
    print(f"{preco_final:.2f}")
else:
    print("Cupom inválido.")
