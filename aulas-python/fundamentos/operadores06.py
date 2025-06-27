# OPERADORES DE ASSOSSIAÇÃO

'''SÃO UTILISADOS PARA VERIFICAR SE UM OBJETO ESTÁ PRESENTE EM UMA SEQUÊNCIA'''

curso = "Curso de Python"
frutas = ["laranja", "uva", "limão"]
saques = [1500, 100]

"python" in curso # python está em curso? True

"maçã" not in frutas # maçã não está em frutas? True

200 in saques # 200 está em saques? False

print("laranja" in frutas)

print("limão" not in frutas)

# case sensitive - reconhece maiúsculas e minúsculas, ou seja os caracteres devem ser idênticos.
print("===================")
print("python" in curso)
print("Python" in curso)