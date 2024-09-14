def main():
    while True:
        A = input().upper().strip()
        B = input().upper().strip()
        sequencia = 0

        for caractere in B:
            if caractere in A:
                sequencia += 1
        print(sequencia)
main()