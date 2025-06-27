#✅ Desafio bônus
#Monte um pequeno cadastro de alunos com:
#Nome
#Idade
#Curso
#Disciplinas (conjunto)
#Cadastre 2 alunos e exiba:
#Os dados de cada um.
#As disciplinas em comum.


# Cadastro de dois alunos com dicionários e conjuntos

print(" Cadastro do Aluno 1 ".center(30, "="))

aluno1 = {} 

aluno1["nome"] = input("Digite o nome do aluno: ")
aluno1["idade"] = int(input("Digite a idade: "))
aluno1["curso"] = input("Digite o curso: ")

disciplinas1 = input("Digite as disciplinas (separadas por vírgula): ")
aluno1["disciplinas"] = {d.strip() for d in disciplinas1.split(",")}


print(" Cadastro do Aluno 2 ".center(30, "="))
aluno2 = {}  

aluno2["nome"] = input("Digite o nome do aluno: ")
aluno2["idade"] = int(input("Digite a idade: "))
aluno2["curso"] = input("Digite o curso: ")

disciplinas2 = input("Digite as disciplinas (separadas por vírgula): ")
aluno2["disciplinas"] = {d.strip() for d in disciplinas2.split(",")}


print(" Dados do Aluno 1 ".center(30, "="))
print("Nome:", aluno1["nome"])
print("Idade:", aluno1["idade"])
print("Curso:", aluno1["curso"])
print("Disciplinas:", aluno1["disciplinas"])

print(" Dados do Aluno 2 ".center(30, "="))
print("Nome:", aluno2["nome"])
print("Idade:", aluno2["idade"])
print("Curso:", aluno2["curso"])
print("Disciplinas:", aluno2["disciplinas"])


comum = aluno1["disciplinas"] and aluno2["disciplinas"]

print(" Disciplinas em comum ".center(30, "="))
if comum:
    print(comum)
else:
    print("Não há disciplinas em comum.")







#produto = {
#    "nome_do_produto" : "Champoo",
#    "preço" : 35,
#    "quantidade_em_estoque" : 10
#
#}
#
#total = produto["preço"] * produto["quantidade_em_estoque"]
#
#print()
#print(" xxx ".center(20, "="))
#print()
#
#print("Nome do produto:", produto["nome_do_produto"])
#print("Preço: R$ ", float(produto["preço"]))
#print("Quantidade em estoque:", produto["quantidade_em_estoque"])
#print()
#print("Valor total do estoque:", total)
#
#print()
#print(" xxx ".center(20, "="))

#===================================

#nomes = ["joão", "maria", "josé", "judas"]
#
#for indice, nome in enumerate(nomes[1:3], start=1):
#    print(f"{indice}: {nome}")

#===================================