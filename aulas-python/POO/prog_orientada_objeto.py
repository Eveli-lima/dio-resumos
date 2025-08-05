# PARADIGMA DA PROGRAMAÇÃO ORIENTADA A OBJETOS

# O QUE É POO?
'''
PARADIGMA DE PROGRAMAÇÃO
    É UM ESTILO DE PROGRAMAÇÃO, NÃO É UMA LINGUAGEM (PYTHON, JAVA, C, ETC), E SIM A FORMA COMO VOCÊ SOLUCIONA OS PROBLEMAS ATRAVÉS DE CÓDIGO.

    EXEMPLO:

    PROBLEMA: beber água
    SOLUÇÃO 1: Usar um copo para beber água.
    SOLUÇÃO 2: Usar uma garrafa para beber água

    ALGUNS PARADIGMAS

    - IMPERATIVO OU PROCEDURAL
    - FUNCIONAL
    - ORIENTADO A EVENTOS

'''
# PROGRAMAÇÃO ORIENTADA A OBJETOS

'''
    O PARADIGMA DE PROGRAMAÇÃO ORIENTADA A OBJETOS ESTRUTURA O CÓDIGO ABSTRAINDO PROBLEMAS EM OBJETOS DO MUNDO REAL, FACILITANDO O ENTENDIMENTO DO CÓDIGO E TORNANDO-O MAIS MODULAR E EXTENSÍVEL. OS DOIS CONCEITOS CHAVES PARA APRENDER POO SÃO: CLASSES E OBJETOS.
'''

# UML - Linguagem de modelagem unificada

'''
DIAGRAMA DE CLASSES:
    Para o diagrama de classes. toda classe é um retângulo. 
    cabeçalho -> Nome da classe: Caneta
    miolo/corpo central -> Todas as características/atributos: modelo, cor, ponta, carga, tampada
    parte de baixo -> todos os métodos: escrever(), rabiscar(), pintar(), tampar(), destampar()

'''
# MODIFICADORES DE VISIBILIDADE

'''
    INDICAM O NÍVEL DE ACESSO AOS COMPONENTES INTERNOS DE UMA CLASSE.

    + PÚBLICA = A classe atual e todas as outras classes possam ter acesso a elas.

    - PRIVADA = Somente a classe atual

    # PROTEGIDA = Da acesso a classe atual e todas as suas sub-classes (herança)

    na parte de chamada só posso mexer se os atributos e métodos forem públicos. se forem privados ou protegidos não posso mexer

'''
# MÉTODOS ESPECIAIS
'''
e = nova Estante - cria um objeto e que é uma estante. isso indica que existe uma classe chamada Estante.
'''

# Métodos Acessores

'''
São métodos que dão acesso a alguma coisa. São oa métodos Getters é o método que vc pega alguma coisa, pegar ou acessar alguma informação.

e = nova Estante
t = e.getTotDoc() - chamando um método, esse método vai até a estante verifica se tem o documento lá e retorna a resposta da quantidade de documentos existentes nessa estante. 

Isso protege o acesso direto ao atributo, dando mais segurança. Não é uma obrigação mas o mercado acaba obrigando por questãoes de segurança.
'''

'''
e = nova Estante
e.totDoc = e.totDoc + 1 - isso acresnta um documento a mais na estante, ,as se mais alguem quiser colocar outro documento pode dar problemas de segurança e organização.
'''
# metodos Modificadores

'''
    Setters - modificam coisas que estão dentro do objeto, garantindo a segurança do atributo

    então ficaria assim:
    e = nova Estante
    e.setTotDoc(doc) - dessa forma ficou mais simples, isso se chama abstração.

    os metodos setters são mais abstratos que os metodos getters
'''

''' PARA CADA ATRIBUTO TENHO QUE TER 2 MÉTODOS EX.: 
CANETA
+ modelo
getModelo()
setModelo(m) - neste caso os seters precisam receber parametros

Classe Caneta
    público modelo: Caractere
    privado ponta: real
    publico Metodo getModelo()
        retorne modelo

    FimMetodo
    publico Metodo setModelo
            (m: caractere)
        modelo = m
    
    FimMetodo
    publico Metodo getPonta()
        retorne ponta
    FimMetodo
    publico Metodo setPonta
            (p:Real)
        ponta = p

FimClasse

c1 = nova Caneta - Agora temos um objeto!
c1.setModelo("Bic Cristal")
c1.setPonta(0.5)
Escreva(c1.getModelo()) 
Escreva(c1.getPonta())
'''

# Método Contrutor

'''
Cosntruct - Eu quero executar uma tarefa sem que um usuário faça uma chamada. Então se eu quiser fazer alguma modificação automaticamente sem a interferência de ninguem eu uso o método contrutor

classe Caneta

    Metodo construtor() - ele sempre vai executar o que estiver dentro desse método automaticamente.
        tampar()
        cor = "Azul"
FimClasse

c1 = nova Caneta - sempre vai criar uma caneta azul tampada pq o método contrutor me indicou isso

O método contrutor pode receber parâmetros:

classe Caneta

    Metodo construtor() 
            (m: Caractere, - modelo
             c: Caractere, - cor
             p: Real)      - ponta
        setModelo(m)
        setCor(c)
        setPonta(p)
        tampar()
FimClasse

c1 = nova Caneta
    ("BIC", "Azul", 0.5)
'''

# Exercício

'''
class ContaBanco

    //atributos
    público numConta: Inteiro
    protegido tipo: Caractere
    privado dono: Caractere
    privado saldo: Real
    privado status: Lógico

    // Metodos Especiais
    publico Metodo Construtor
        saldo = 0
        status = falso
    FimMetodo
    publico Metodo setNumConta(n:inteiro)
        numConta = n
    FimMetodo
    publico Metodo getNumConta()
        return numConta
    FimMetodo
    publico Metodo setTipo(t:Caractere)
        tipo = t
    FimMetodo
    publico Metodo getTipo()
        return tipo
    FimMetodo
    publico Metodo setDono(d:Caractere)
        dono = d
    FimMetodo
    publico Metodo getDono()
        return dono
    FimMetodo
    publico Metodo setSaldo(s:Real)
        saldo = s
    FimMetodo
    publico Metodo getSaldo()
        return saldo
    FimMetodo
    publico Metodo setStatus(s:Lógico)
        status = s
    FimMetodo
    publico Metodo getStatus()
        return status
    FimMetodo

    //Métodos
    publico Metodo abrirConta(t:Caractere)
        setTipo(t)
        setStatus(verdadeiro)
        se (t = "CC") então
            saldo = 50
        senão se (t = "CP") então
            saldo = 150
        FimSe
    FimMetodo

    publico Metodo fecharConta()
        se (saldo > 0) então
            Escreva("Conta com dinheiro")
        senão se (saldo < 0) então
            Escreva("Conta em débito")
        senão
            setStatus(false)
        FimSe
    FimMetodo

    publico Metodo depositar(v:Real)
        se (status = verdadeiro) então
            setSaldo(getSaldo() + v) 👈 = 👉 saldo = saldo + v
        senão
            Escreva("Impossível depositar")
        FimSe

    publico Metodo sacar(v:Real)
        se (status = verdadeiro) então
            se (getSaldo > v) então
                setSaldo(getSaldo() - v)
            senão
                Escreva("Saldo Insuficiente)
            FimSe
        senão
            Escreva("Impossivel sacar")
        FimSe
    FimMetodo

    publico Metodo pagarMensal()
        var v: Real
        se (tipo ="CC") então
            v = 12
        senão se (tipo = "CP") então
            v = 20
        FimSe
        se (status = verdadeiro) então
            se (saldo > v) então
                setSaldo(getSaldo() - v)
            senão
                Escreva("Saldo insuficiente")
            FimSe
        senão
        Escreva("Impossível pagar")
    FimMetodo

    publico Metodo abrirConta()
        (...)
    FimMetodo
    publico metodo fecharConta()
        (...)
    FimMetodo
    publico metodo depositar()
        (...)
    FimMetodo
    publico metodo sacar()
        (...)
    FimMetodo
    publico metodo pagarMensal()
        (...)
    FimMetodo
FimClasse
'''