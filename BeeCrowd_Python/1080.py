#ENTRADA
def main():
    num_referencia = -1
    posicao_num = -1
    contador = 1

#PROCESSO
    while contador <= 100:
        valor = int(input())

        if valor > num_referencia:
            num_referencia = valor
            posicao_num = contador

            contador += 1
    
    print(num_referencia)
    print(posicao_num)


main()