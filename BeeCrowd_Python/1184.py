def main():
    O = input().upper()

    # CRIANDO UMA MATRIZ 12X12 VAZIA
    matriz = criar_matriz(12,12)

    # PREENCHENDO ESSA MATRIZ VAZIA
    preenchendo_matriz(matriz)

    # RESULTADO
    resultado = operacao_na_area(matriz, O)

    print("{:.1f}".format(resultado))

# FUNÇÃO QUE GERA MINHA MATRIZ VAZIA
def criar_matriz(linhas,colunas):
    matriz_vazia = []

    for linha in range(linhas):
        matriz_vazia.append([0.0] * colunas)

    return matriz_vazia

# FUNÇÃO QUE IRÁ PREENCHER MINHA MATRIZ
def preenchendo_matriz(matriz_):

    for linha in range(len(matriz_)):
        for coluna in range(len(matriz_[linha])):
            matriz_[linha][coluna] = float(input())

    return matriz_

# FUNÇÃO QUE APLICA ALGO SOBRE OS ELEMENTOS QUE ESTÃO NA AREA
def operacao_na_area(matriz_,operacao):
    soma = 0
    contador = 0

    for linha in range(1,12):
        for coluna in range(0,linha):
            soma += matriz_[linha][coluna]
            contador += 1
                   
    if operacao == 'S':
        return soma
    else:
        return soma / contador

main()

