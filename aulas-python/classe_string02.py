# INTERPOLAÇÃO DE VARIÁVEIS

'''TEMOS 3 FORMAS DE INTERPOLAR VARIÁVEIS EM STRINGS, 1° É USANDO O SINAL %, A 2° É UTILIZANDO O MÉTODO FORMAT E A ÚLTIMA É UTILIZANDO f strings.
A PRIMEIRA FORMA NÃO É RECOMENDADA E SEU USO É RARO, VAMOS FOCAR NAS DUAS ÚLTIMAS
'''

# %s = QUANDO VC QUISER COLOCAR VALORES TIPO STRINGS
# %d = PARA VALORES INTEIROS
# %f = PARA PONTOS FLUTUANTES

# Método Old style %

nome = "Éveli"
idade = 37
profissao = "programadora"
linguagem = "Python"

print()
print("old style".center(21, "*"))
print() 

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculada no curso de %s." % (nome, idade, profissao, linguagem))

print()
print("Format".center(21, "*"))
print()

# Método format

print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculada no curso de {}." .format(nome, idade, profissao, linguagem))

print()
print("Format com indice".center(33, "*"))
print()

print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculada no curso de {0}." .format(linguagem, profissao, idade, nome))

print()
print("Format com variáveis".center(32, "*"))
print()

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

print()
print("Format com dicionário".center(32, "*"))
print()

dados = {"nome": "Éveli", "idade": 37, "profissao": "programadora"
"linguagem": "Python" }

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como #{profissao} e estou matriculado no curso de {linguagem}.".format(**pessoa))

print()
print("f-strings".center(22, "*"))
print()
# Método f-strings

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")

print()
print("formatação".center(22, "*"))
print()

PI = 3.14159

print(PI)

print(f"Valor de PI: {PI:.2f}")

print(f"Valor de PI: {PI:10.2f}")