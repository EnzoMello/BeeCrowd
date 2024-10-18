def main():
    N = int(input())

    contador = 1
    while contador <= N:
        print(f"{contador} {contador + 1} {contador + 2} PUM")
        contador += 4

if __name__ == "__main__":
    main()
