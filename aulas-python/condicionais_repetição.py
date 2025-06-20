# IDENTAÇÃO E BLOCOS

'''IDENTAR CÓDIGO É UMA FORMA DE MANTER O CÓDIGO FONTE MAIS LEGÍVEL E MANUTENÍVEL. ALÉM DISSO, NO PYTHON, O INTERPRETADOR CONSEGUE DETERMINAR ONDE UM BLOCO DE COMANDO INICIA E ONDE ELE TERMINA.'''

# UTILIZANDO ESPAÇOS

'''EXISTE UMA CONVENÇÃO EM PYTHON, QUE DEFINE AS BOAS P´RATICAS DE CÓDIGO NA LINGUAGEM. É INDICADO UTILIZAR 4 ESPAÇOS EM BRANCO POR NÍVEL DE IDENTAÇÃO.'''

#def sacar(self, valor: float) none: # INÍCIO DO BLOCO  DO MÉTODO
#    if self.saldo >= valor:         #INICIO DO BLOCO if, nessa linha tem 4 espaços no inicio e dois pontos no final significa que eu abri um bloco.
#        self.saldo -= valor #mais 4 espaços estou dentro do bloco
#'''o recuo dos espaços insica o fechamento dos blocos'''
#    # FIM DO BLOCO if
##FIM DO BLOCO DO MÉTODO

def sacar(valor): #abertira do método nos dois pontoa (:)
    saldo = 500   # o que está aqui dentro faz parte do método sacar

    if saldo >= valor:
        print("valor sacado!") # aqui é o que está dentro do bloco if
        print("Retire seu dinheiro na boca do caixa.") #Essas duas mensagens dentro do bloco só vão aparecer se o saque deu certo.
    print("Obrigado por ser nosso cliente, Tenha um bom dia!") # Se o saque der errado vai aparecer apenas ewsa msm.
    # aqui é o final fo bloco if

# quando voltar a identação original do método que é essa significa o final do método.

def depositar(valor):
    saldo = 500
    saldo += valor
    print("Saldo atual: ", saldo)


sacar(100)
depositar(200)