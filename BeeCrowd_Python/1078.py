#ENTRADA
def main():
    N = int(input())

 contador = 1

#PROCESSAMENTO
    while contador<=10:
       calculo = contador * N
       print(f"{contador} x {N} = {calculo}")
       contador +=1

main()

