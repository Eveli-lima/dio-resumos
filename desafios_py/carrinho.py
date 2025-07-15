"""Crie um sistema de carrinho de compras que permita adicionar produtos e calcular o valor total da compra.

Entrada
Lista de produtos adicionados ao carrinho (cada um com nome e preço).
Saída
Lista dos produtos adicionados e o total da compra."""

# Lista para armazenar os produtos e preços
carrinho = []
total = 0.0

# Entrada do número de itens
n = int(input().strip())

# Loop para adicionar itens ao carrinho
for _ in range(n): # O _ é só um nome qualquer para a variável do loop — usamos assim quando não vamos usá-la.
    linha = input().strip()
    
    # Encontra a última ocorrência de espaço para separar nome e preço
    posicao_espaco = linha.rfind(" ") 

    """📌 O que é str.rfind()?
    É um método de string em Python que procura a última ocorrência de uma substring (ou pedaço de texto) dentro de uma string maior. O "r" de rfind vem de "right" — ele começa a procurar da direita para a esquerda, mas ainda retorna o índice normal (da esquerda para a direita)."""
    
    # Separa o nome do produto e o preço
    item = linha[:posicao_espaco]
    preco = float(linha[posicao_espaco + 1:])
    
    # Adiciona ao carrinho
    carrinho.append((item, preco))
    total += preco

# TODO: Exiba os itens e o total da compra
for nome, preco in carrinho:
    print(f"{nome}: R$ {preco:.2f}")
print(f"Total: R$ {total:.2f}")
