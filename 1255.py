def main():
    n = int(input(""))

    for caso in range(n):
        frase = input().lower()
        caracteres = {}
        maior = 0
        letra_ganhadora = ''

        for letra in frase:
            if letra.isalpha() and letra not in caracteres:
                caracteres['{}'.format(letra)] = 0
                valor = caracteres['{}'.format(letra)]
                soma = valor + frase.count(letra) 
                caracteres['{}'.format(letra)] += soma


        for letra in caracteres:
            if caracteres['{}'.format(letra)] > maior:
                maior = caracteres['{}'.format(letra)]
                letra_ganhadora = letra
            elif caracteres['{}'.format(letra)] == maior:
                letra_ganhadora += letra

        print(letra_ganhadora)
            
main()