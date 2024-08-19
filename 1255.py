def main():
    n = int(input(""))

    for caso in range(n):
        frase = input().lower()
        caracteres = {}
        maior = str()

        for letra in frase:
            if letra.isalpha() and letra not in caracteres:
                caracteres += frase.count(letra)

        for letra in caracteres:
            if letra > maior:
                maior = caracteres[letra]
       
        print(maior)
            
main()