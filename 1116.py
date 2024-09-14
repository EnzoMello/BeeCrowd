def main():
    n = int(input())
    contador = 0
    while contador < n:
        x, y = map(int, input().split())
        if y != 0:
            resultado = x / y
            print("%.1f" % resultado)
        else:
            print("divisao impossivel")
        contador += 1

if __name__ == "__main__":
    main()
