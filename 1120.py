def main():

    while True:
        verificacao = input().split()
        numero_falho = verificacao[0]
        valor = verificacao[1]

        if numero_falho == '0' and valor == '0':
            break
        else:
            valor = valor.replace(numero_falho, "")
            if valor == "":
                valor = 0
            else:
                valor = int(valor)

            print(valor)

                
main()