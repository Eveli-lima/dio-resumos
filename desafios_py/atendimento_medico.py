n = int(input().strip())

# Lista para armazenar pacientes
pacientes = []

# Loop para entrada de dados
for _ in range(n):
    nome, idade, status = input().strip().split(", ")
    idade = int(idade)
    pacientes.append((nome, idade, status))

# TODO: Ordene por prioridade: urgente > idosos > demais:
def paciente_prioridade(paciente):
    if paciente[2] == "urgente":
        return (0, -paciente[1])
    elif paciente[1] >= 60:
        return (1, -paciente[1])
    else:
        return (2, -paciente[1])
        
pacientes_ordenados = sorted(pacientes, key=paciente_prioridade)
nomes = [paciente[0] for paciente in pacientes_ordenados]

    
# TODO: Exiba a ordem de atendimento com título e vírgulas:
print(f"Ordem de atendimento: {', '.join(nomes)}")






