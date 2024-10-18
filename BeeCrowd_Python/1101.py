def sequencia_e_soma(m, n):
    menor = min(m, n)
    maior = max(m, n)
    soma = 0
    sequencia = ""
    num = menor
    while num <= maior:
        sequencia += str(num) + " "
        soma += num
        num += 1
    return sequencia[:-1], soma

def main():
    continuar = True
    while continuar:
        m, n = input().split()
        m = int(m)
        n = int(n)
        if m <= 0 or n <= 0:
            continuar = False
        else:
            sequencia, soma = sequencia_e_soma(m, n)
            print(f"{sequencia} Sum={soma}")

if __name__ == "__main__":
    main()
