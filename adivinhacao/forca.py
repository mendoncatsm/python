import random


def jogar():

    imprime_mensagem_inicial()
    palavra_secreta = carrega_palavra()

    enforcou = False
    acertou = False
    letras_acertadas = []
    for letra in palavra_secreta:
        inicializa_palavra_secreta(palavra_secreta)
    erros = 0
    letras_erradas=[]
    print(letras_acertadas)
    while(not enforcou and not acertou):
        print("Você tem {} tentativas restantes".format(6-erros))
        tentativa = input("digite uma letra:")
        tentativa = tentativa.strip().upper()

        index = 0
        if tentativa in palavra_secreta:
            for letra in palavra_secreta:
                if(tentativa.upper()==letra.upper()):
                    letras_acertadas[index] = letra
                index = index + 1
        elif tentativa in letras_erradas:
            print("Letra repetida")
        else:
            erros +=1
            letras_erradas.append(tentativa)
        enforcou = erros==6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
        print("Erradas: {}".format(letras_erradas))

    if (acertou):
        print("Você ganhou!")
    else:
        print("você perdeu")
    print("Fim de jogo")



def imprime_mensagem_inicial():
    print("*********************************")
    print("Bem vindos ao jogo de Forca")
    print("*********************************")

def carrega_palavra():

    arquivo = open("palavras.txt", "r")
    palavra = []

    for linha in arquivo:
        palavra.append(linha.strip())

    arquivo.close()

    numero = random.randrange(0,len(palavra))

    palavra_secreta=palavra[numero].upper()
    return palavra_secreta


def inicializa_palavra_secreta(palavra):
    return ["_" for letra in palavra]

if(__name__=="__main__"):
    jogar()
