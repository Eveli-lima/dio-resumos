# STRING MÚLTIPLAS LINHAS

'''STRINGS DE MÚLTUPLAS LINHAS SÃO DEFINIDAS INFORMANDO 3 ASPAS SIMPLES OU DUPLAS DURANTE A ATRIBUIÇÃO. ELAS PODEM OCUPAR VÁRIAS LINHAS DO CÓDIGO, E TODOS OS ESPAÇOS EM BRANCO SÃO INCLUÍDOS NA STRING FINAL'''

nome = "Eveli"

mensagem = f"""
Olá meu nome é {nome}, Eu estou aprendendo Python
"""

print(mensagem)

msn = f'''
    Olá meu nome é {nome}, 
Eu estou aprendendo Python
    Essa mensagem tem diferentes recuos.
'''
print(msn)

print(
    '''
    ========== Menu ==========
    
    1 - Depositar
    2 - Sacar
    0 - Sair

    ==========================

    Obrigado por usar nosso sistema!!!!
    
'''
)







