# OS CONCEITOS DE CLASSES E OBJETOS

'''
UMA CLASSE DEFINE AS CARACTERÍSTICAS E COMPORTAMENTOS DE UM OBJETO, PORÉM NÃO CONSEGUIMOS USÁ-LAS DIRETAMENTE, JÁ OS OBJETOS PODEMOS USÁ-LOS E ELES POSSUEM AS CARACTERÍSTICAS E COMPORTAMENTOS QUE FORAM DEFINIDOS NAS CLASSES.
'''

class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def latir(self):
        print("Auau")

    def dormir(self):
        self.acordado = False
        print("Zzzzz...")

cao_1 = Cachorro("Chappie", "amarelo", False)
cao_2 = Cachorro("Aladim", "branco e preto")

cao_1.latir()

print(cao_2.acordado)
cao_2.dormir()
print(cao_2.acordado)

# classe = classificar; objeto = coisa material ou abstrata que pode ser percebida pelos sentidos e descritas por meio das suas caracteristicas, comportamentos e estado atual

''' UMA CLASSE TEM QUE RESPONDER SEMPRE A 3 PERGUNTAS.'''

# QUE COISAS EU TENHO? = atributo
# QUE COISAS EU FAÇO? = método
# COMO EU ESTOU AGORA? = estado

# EXEMPLO:

# QUE COISAS UMA CANETA TEM?
# modelo, cor, ponta, carga, tampada

# QUE COISAS UMA CANETA FAZ?
# escrever, rabiscar, pintar, tampar, destampar

# QUAL O ESTADO DA CANETA?
# nesse momento a caneta está com 50% de carga, tem a ponta fina, está destampada e escrevendo.

''' sempre que falar de atributo posso dizer tbm propriedades, características, dados. quando falar de comportamento, está falando dos métodos, procedimentos, rotinas internas desse objeto, e quando fala de estado, está se referiando as caracteristicas atuais no momento em que eu to analisando esse objeto'''

# TODO OBJETO VEM A PARTIR DE UMA CLASSE OU TODO OBJETO VEM A PARTIR DE UM MOLDE

# INSTANCIAMENTO:

'''
E QUANDO EU TENHO UMA CLASSE E QUERO TRASFORMAR ELA EM UM OBJETO TEM UM NOME PARA ISSO: INSTANCIAMENTO. ENTÃO INSTANCIAR É PEGAR UMA CLASSE E CONSIGO GERAR UM OBJETO A PARTIR DELA. EU NÃO TRANSFORMO UMA CLASSE EM OBJETO EU GERO UM OBJETO A PARTIR DE UMA CLASSE.

ENTÃO QUANDO EU CRIO UM OBJETO, EU DIGO: EU ESTOU INSTANCIANDO UMA CLASSE EM FORMA DE UM OBJETO.
'''

# ABSTRAÇÃO:

''' 
É CONSIDERADO O PRIMEIRO PILAR DA PROGRAMAÇÃO ORIENTADA A O BJETO

SE EU COLOCAR UM ATRIBUTO COMO PÚBLICO TD MUNDO VAI PODER USAR ESSE ATRIBUTO LIVREMENTE.

JÁ NO CASO DO PRIVADO, SOMENTE A CLASSE ATUAL VAI TER ACESSO

UM MÉTODO OU ATRIBUTO PROTEGIDO DÁ ACESSO A CLASSE ATUAL E A TODAS AS SUAS SUB CLASSES 
'''

