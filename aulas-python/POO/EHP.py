# Pilares da programação orientada a objeto

'''
EHP
E - Encapsulamento -- Para o guanabara a Abstração está dentro do Encapsulamento
H - Herança
P - Polimorfismo

'''
# ou

'''
AEHP

A - Abstração
E - Encapsulamento
H - Herança
P - Polimorfismo

'''
# ENCAPSULAMENTO

'''
A CÁPSULA, COMO A DE UMA PILHA, POR EXEMPLO, SERVE PARA PROTEGER E CRIAR UM PADRÃO

ENCAPSULAR EM POO É OCULTAR PARTES INDEPENDENTES DA IMPLEMENTAÇÃO, PERMITINDO CONSTRUIR PARTES INVISÍVEIS AO MUNDO EXTERIOR.

PODEMOS CONVERSAR COM ESSA CÁPSULA, CONVERSAR COM OBJETOS, POR MEIO DE MENSAGENS QUE VÃO GERAR RESPOSTAS SEM QUE PRECISE ENTRAR NA CÁPSULA

ESSE CANAL DE COMUNICAÇÃO EXTERNA QUE TD OBJETO TEM SE CHAMA INTERFACE

INTERFACE É UMA LISTA DE SERVIÇOS FORNECIDO POR UM COMPONENTE. É O CONTATO COM O MUNDO EXTERIOR, QUE DEFINE O QUE PODE SER FEITO COM UM OBJETO DESSA CLASSE.

ENCAPSULAR *NÃO É OBRIGATÓRIO* MAS É UMA BOA PRÁTICA PARA PRODUZIR CLASSES MAIS EFICIENTES

VANTAGENS:

1. TORNAR MUDANÇAS INVISIVEIS
2. FACILITAR A REUTILIZAÇÃO DO CÓDIGO
3. REDUZIR OS EFEITOS COLATERAIS
'''
# COMO ENCAPSULAR?

'''
UMA INTERFACE É PARECIDO COM A CLASSE MAS NÃO TEM ATRIBUTOS SÓ TEM MÉTODOS

|------------------|
|  <<interface>>   |
|   Controlador    |
|------------------|
| + ligar()        |
| + desligar()     |
| + abrirMenu()    |
| + fecharMenu()   |
| + maisVolume()   |
| + menosVolume()  |
| + ligarMudo()    |
| + desligarMudo() |
| + play()         |
| + pause()        |
|------------------|

Esses métodos se chamam métodos abstratos, são aqueles métodos que não vai ser desenvolvidos na interface, ele vai existir porem não será acessado. Isso é método abstrado que é previsto mas não implementado.

E em uma interface tds os métodos são definidos como públicos

Com a interface definida podemos definir a classe

|------------------|
|  ControleRemoto  |
|------------------|
|  - volume        |  -> atributos
|  - ligado        |
|  - tocando       |
|------------------|
| + ligar()        |  -> metodos da interface
| + desligar()     |
| + abrirMenu()    |
| + fecharMenu()   |
| + maisVolume()   |
| + menosVolume()  |
| + ligarMudo()    |
| + desligarMudo() |
| + play()         |
| + pause()        |
| - setVolume()    |  -> metodos especiais (privado para esse exercício)
| - getVolume()    |
| - setLigado()    |
| - getLigado()    |
| - setTocando()   |
| - getTocando()   |
|------------------|

QUANDO VOCÊ ENCAPSULA A PRIMEIRA COISA A SE FAZER É TORNAR TDS OS ATRIBUTOS PRIVADOS

Copiar os métodos do controlador para a classe controleRemoto e acrescentar os métodos adicionais por exemplo os métodos especiais, o get e o set. pois os atributos estão privados.
'''
# Criando interface

'''
interface Controlador
    //Métodos Abstratos
    publico abstrato Metodo ligar()
    publico abstrato Metodo desligar()
    publico abstrato Metodo abrirMenu()
    publico abstrato Metodo fecharMenu()
    publico abstrato Metodo maisVolume()
    publico abstrato Metodo menosVolume()
    publico abstrato Metodo ligarMudo()
    publico abstrato Metodo desligarMudo()
    publico abstrato Metodo play()
    publico abstrato Metodo pause()
FimInterface

'''
# Criando Classe

'''
Classe ControleRemoto 

    //Atributos
    privado inteiro volume
    privado logico ligado
    privado logico tocando

    //métodos especiais
    publico metodo construtor()
        volume = 50
        ligado = falso
        tocando = falso
    FimMetodo
    privado metodo getVolume()
        retorne volume
    FimMetodo
    privado metodo getLigado()
        retorne volume
    FimMetodo
    privado metodo getTocando()
        retorne volume
    FimMetodo
    privado metodo setVolume(v: Inteiro)
        volume = v
    FimMetodo
    privado metodo setLigado(l: logico)
        ligado = l
    FimMetodo
    privado metodo setTocando(t: logico)
        Tocando = t
    FimMetodo
FimClasse

classe ControleRemoto implementa Controlador

    // Sobrescrever métodos
    publico metodo ligar()
        setLigado(verdadeiro)
    FimMetodo
    publico metodo desligar()
        setLigado(falso)
    FimMetodo
    publico metodo abrirMenu()
        Escreva(getLigado())
        Escreva(getVolume())
        para i = 0 ate getVolume() passo 10 faca
            Escreva("|")
        FimPara
        Escreva(getTocando())
    FimMetodo
    publico metodo fecharMenu()
        Escreva("Fechando Menu...")
    FimMetodo
    publico metodo maisVolume()
        se (getLigado()) então
            setVolume(getVolume() + 1)
        FimSe
    FimMetodo
    publico metodo menosVolume()
        se (getLigado()) então
            setVolume(getVolume() - 1)
        FimSe
    FimMetodo
    publico metodo ligarMudo()
        se (getLigado() e getVolume() > 0) então
            setVolume(0)
        FimSe
    FimMetodo
    publico metodo desligarMudo()
        se (getLigado() e getVolume() = 0) então
            setVolume(50)
        FimSe
    FimMetodo
    publico metodo play()
        se (getLigado() e nao getTocando()) então
            setTocando(verdadeiro)
        FimSe
    FimMetodo
    publico metodo pause()
        se (getLigado() e getTocando()) então
            setTocando(falso)
        FimSe
    FimMetodo
FimClasse
'''
