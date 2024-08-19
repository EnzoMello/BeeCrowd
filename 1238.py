def main():
    qtd_palavras = int(input())

    for elemento in range(qtd_palavras):
        texto = input().split()
        palavra_1 = texto[0]
        palavra_2 = texto[1]
        texto_final = ''

        if len(palavra_1) <= len(palavra_2):
            for caractere in range(len(palavra_1)):
                texto_final += palavra_1[caractere]
                texto_final += palavra_2[caractere]
            texto_final += palavra_2[len(palavra_1):]
        else:
            for caractere in range(len(palavra_2)):
                texto_final += palavra_1[caractere]
                texto_final += palavra_2[caractere]
            texto_final += palavra_1[len(palavra_2):]

        print(texto_final)
main()