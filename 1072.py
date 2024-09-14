def main():
    N = int(input())
    dentro_intervalo = 0
    fora_intervalo = 0
    contador = 0

    while contador < N:
        X = int(input())
        if 10 <= X <= 20:
            dentro_intervalo += 1
        else:
            fora_intervalo += 1
        contador += 1

    print(f"{dentro_intervalo} in")
    print(f"{fora_intervalo} out")

if __name__ == "__main__":
    main()
