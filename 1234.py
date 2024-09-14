def main():
    while True:
        entrada = input()
        if entrada == 'EOF':
            break
        else:
            saida = ''
            verificador = 0
            # PARA CADA LETRA EM ENTRADA, A LETRA É ADICIONADA NA SAIDA DE FORMA MAIÚSCULA OU MINÚSCULA DE ACORDO COM O VERIFICADOR
            for letra in entrada:
                if verificador == 0 and letra != ' ':
                    saida += letra.upper()
                    verificador = 1
                elif verificador == 1 and letra != ' ':
                    saida += letra.lower()
                    verificador = 0
            # SE FOR ESPAÇO, ENTÃO SERÁ O CASO ELSE DAS VERIFICAÇÕES
                else:
                    saida += ' '

            print(saida)


main()