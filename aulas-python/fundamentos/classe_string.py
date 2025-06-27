# MÉTODOS ÚTEIS DA CLASSE STRING

'''A CALASSE STRING EM PYTHON É RICA EM MÉTODOS'''

# MINÚSCOLA, MIÚSCULA E TÍTULO

curso = "pYtHon"

print("*********maiúsculas**************")

print(curso.upper()) # >>> PYTHON

print("**********minúsculas*************")

print(curso.lower()) # >>> python

print("**********Título*************")

print(curso.title()) # >>> Python

# ELIMINANDO ESPAÇOS EM BRANCO

print()
print("espaços".center(21, "*"))

curso = "   Python  "

print("****remover espaços dos dois lados*****")

print("###", curso.strip(), "###") # >>> ### Python ###

print("**********remove da esquerda*************")

print("###", curso.lstrip(), "###") # >>> ### Python   ###

print("**********remove da direita*************") # >>> ###    Python ###

print("###", curso.rstrip(), "###")

print()
print("centralizar e junções".center(41, "*"))


# JUNCÕES E CENTRALIZAÇÃO

curso = "Python"

print(curso.center(10, "#")) # >>> ##Python## (Útil para cirar e centralizar menus)
print(curso.center(10, "_")) # >>> __Python__

print(".".join(curso)) # >>> P.y.t.h.o.n



