def main():
    x = int(input())
    y = int(input())

    if x > y:
        x, y = y, x

    soma = 0
    num = x

    while num <= y:
        if num % 13 != 0:
            soma += num
        num += 1
    
    print(soma)

if __name__ == "__main__":
    main()