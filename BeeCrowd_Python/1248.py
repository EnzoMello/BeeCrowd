def main():
    n = int(input())

    for caso in range(n):
        dieta = input().upper()
        cafe = input().upper()
        almoco = input().upper()
        lista_dieta = []
        lista_comeu = []

        ja_comeu = cafe + almoco
        
        for comida in ja_comeu:
            valor = ord(comida[0])
            lista_comeu.append(valor)

        for alimento in dieta:
            valor_alimento = ord(alimento[0])
            lista_dieta.append(valor_alimento)

        if ja_comeu not in dieta:
            print("CHEATER")
        else:
            jantar = [item for item in lista_dieta if item not in lista_comeu]

            for codigo in jantar:
                valor3 = chr(codigo)

        print(jantar)

main()