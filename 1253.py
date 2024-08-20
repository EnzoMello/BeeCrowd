def main():
    # LEIO UMA QUANTIA REFERENTE À QUANTIDADE DE CASOS DE TESTE
    n = int(input())

    for caso in range(n):
        palavra_codificada = input().upper()
        intervalo = int(input())
        palavra_transcrita = ''

        for letra in palavra_codificada:
            caractere = ord(letra[0])
            transcrevendo = caractere - intervalo

            if transcrevendo < 65:
                transcrevendo = caractere - intervalo + 26
        
            transcrito = chr(transcrevendo)
            palavra_transcrita += transcrito
        
        print(palavra_transcrita)
main()