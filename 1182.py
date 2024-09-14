def main():
    # PEDINDO OS DADOS DA ENTRADA DA QUESTÃO
    coluna = int(input())
    operacao = input().upper()

    # CRIANDO A MATRIZ
    matriz = gerando_matriz(12,12)

    # COMO A MATRIZ 12X12 ESTÁ VAZIA, EU VOU PREENCHER OS 144 ELEMENTOS DELA
    preencher_matriz(matriz)

    # COM A MATRIZ JÁ PREENCHIDA, FAÇO A OPERAÇÃO NA COLUNA DESEJADA
    final = operacao_matriz(matriz, operacao, coluna)

    print("{:.1f}".format(final))

# FUNÇÃO QUE CRIA UMA MATRIZ VAZIA
def gerando_matriz(linhas, colunas):
    matriz_vazia = []

    for linha in range(linhas):
            matriz_vazia.append([0.0] * colunas)
    
    return matriz_vazia 

# FUNÇÃO QUE PREENCHE CADA ELEMENTO DA MATRIZ VAZIA
def preencher_matriz(exemplo):

    for linha in range(len(exemplo)):
        for coluna in range(len(exemplo[linha])):
            exemplo[linha][coluna] = float(input())

# FUNÇÃO QUE APLICA UMA OPERAÇÃO NA COLUNA X DA MATRIZ
def operacao_matriz(matriz_, operacao_, coluna):
    soma = 0
    contador = 0

    for linha in range(len(matriz_)):
            soma += matriz_[linha][coluna]
            contador += 1
    
    media = soma / contador

    if operacao_ == "S":
        return soma
    else:
        return media

main()
