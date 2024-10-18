def main():
    N = int(input())
    valores = input().split()
    
    # DESCOBRINDO MENOR VALOR E SUA POSIÇÃO
    menor_valor = min(incrementa_lista(N, valores))
    menor_posicao = valores.index(str(menor_valor))

    print('''Menor valor: {}
Posicao: {}'''.format(menor_valor, menor_posicao))

# FUNÇÃO QUE RETORNA LISTA JÁ INCREMENTADA
def incrementa_lista(intervalo, valores):
    minha_lista = []
    
    for elemento in range(intervalo):
        minha_lista.append(int(valores[elemento]))

    return minha_lista

main()