import random

def jogar():
    print("*********************************")
    print("Bem vindos ao jogo de adivinhação")
    print("*********************************")

    numero_secreto = random.randrange(1,101)
    print(numero_secreto)


    numero_tentativas = 3

    for rodada in range(1,numero_tentativas+1):
        print("Tentativa {} de {}" .format(rodada,numero_tentativas))
        tentativa_str = input("Digite um número de 1 a 100:")
        print("voce digitou", tentativa_str)
        tentativa = int(tentativa_str)

        if(tentativa < 1 or tentativa > 100):
            print("Erro!Digite um valor entre 1 e 100!")
            continue

        acertou = numero_secreto==tentativa
        maior = tentativa>numero_secreto
        menor = tentativa<numero_secreto

        if(acertou):
            print("Você acertou!")
            break
        else:
            if(maior):
                print("Você errou. O numero tentado foi maior")
            elif(menor):
                print("Você errou. O numero tentado é menor")
if(__name__=="__main__"):
    jogar()

