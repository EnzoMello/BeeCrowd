#ENTRADA
def main():
    x = int(input())
    y = int(input())

#PROCESSO
    if x > y:
        inicio = y
        fim = x
    else:
        inicio = x
        fim = y

    num = inicio + 1

#SAÍDA
    while num < fim:
        if num % 5 == 2 or num % 5 == 3:
            print(num)
        num += 1

if __name__ == "__main__":
    main()
