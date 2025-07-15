eventos = {}
n = int(input(""))

for _ in range(n):
    linha = input("")
    partes = linha.split(",")
    nome = partes[0].strip()
    tema = partes[1].strip()

    if tema in eventos:
        eventos[tema].append(nome)
    else:
        eventos[tema] = [nome]

for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")


    #TEXTES -  como adicionar valores em um dicionário

#contatos = {}
#
#nome = input("digite o nome: ")
#idade = input("Digite a idade: ")
#telefone = input("Digite o telefone: ")
#
##outro dicionário
#contatos[nome] = {
#    "idade": idade,
#    "Telefone": telefone
#}
#
##lista
#contatos[nome] = [idade, telefone]
#
#print(contatos)

##Exemplo: Dicionário com listas como valores
##Digamos que você quer armazenar vários telefones ou várias notas, ou qualquer outra coisa que venha em lista.

#frutas_favoritas = {}
#
#nome = input("Digite o nome: ")
#frutas = input("Digite as frutas favoritas separadas por vírgula: ")
#
#lista_de_frutas = frutas.split(",")  # transforma a string em lista
#
#lista_de_frutas = [f.strip() for f in frutas.split(",")]
#
#frutas_favoritas[nome] = lista_de_frutas
#
#print(frutas_favoritas)
#
###Você também pode usar um loop para permitir que o usuário adicione quantos itens quiser:
#
#
#contatos = {}
#
#nome = input("Digite o nome: ")
#contatos[nome] = []
#
#while True:
#    telefone = input("Digite um telefone (ou 'fim' para parar): ")
#    if telefone.lower() == "fim":
#        break
#    contatos[nome].append(telefone)
#
#print(contatos)



