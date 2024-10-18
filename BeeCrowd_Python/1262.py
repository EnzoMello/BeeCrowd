def main():
    processamento = input().upper()
    rastro = len(processamento)
    numero_leituras_simultaneas = int(input())
    numero_ciclos = 0
    count_r = 0

    for letra in range(rastro):
        
        if letra == 'W':
            numero_ciclos += 1

        if letra == 'R' and count_r < numero_leituras_simultaneas:
            count_r += numero_leituras_simultaneas
            numero_ciclos += 1
        elif rastro[letra + 1] == 'R' and count_r == numero_leituras_simultaneas:
            count_r = 0 

    print(numero_ciclos)
    
main()