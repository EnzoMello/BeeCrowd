def soma_impares_entre(x, y):
    soma = 0
    num = x
    while num <= y:
        if num % 2 != 0:
            soma += num
        num += 1
    return soma

def main():
    casos_teste = int(input("Digite a quantidade de casos de teste: "))

    while casos_teste > 0:
        x, y = map(int, input().split())
        print(soma_impares_entre(x, y))
        casos_teste -= 1

if __name__ == "__main__":
    main()
