def main():
    N = int(input())
    for caso in range(N):
        valores = input().split()
        A = valores[0]
        B = valores[1]
        count_b = 0

        for i in range(len(B)):
            count_b += 1
            
        string_a = str(A)[-count_b:]
        string_b = str(B)

        if len(string_b) > len(string_a):
            print("nao encaixa")
        elif string_b in string_a:
            print("encaixa")
        else:
            print("nao encaixa")
main()