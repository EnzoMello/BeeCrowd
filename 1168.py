# CADA DÍGITO É FORMADO POR UM "PAUZINHO" E ELES CORRESPONDEM AO NÚMERO DE LEDS NECESSÁRIOS PARA ACENDER TAL DÍGITO

def main():
    pauzinhos = [6,2, 5, 5, 4, 5, 6, 3, 7, 6,]

    # LEIO O VALOR N CORRESPONDENTE AO NÚMERO DE CASOS DE TESTE
    n = int(input())

    # UM NOVO CASO TESTE PARA CADA VALOR EM N CASOS DE TESTE
    for caso in range(n):
        valor = input()
        leds_totais = 0
        
        # CADA DIGITO(STR) EM VALOR SERÁ IGUAL A UM INTEIRO EM PAUZINHOS E SERÁ INCREMENTADO ESSE VALOR EM leds_totais
        for digito in valor:
            leds_totais += pauzinhos[int(digito)]

        print("{} leds".format(leds_totais))
main()