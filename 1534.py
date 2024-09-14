def main():
    while True:
        try:
            N = input()
            if N == 'EOF':
                break
            else:
                n_numero = int(N)
                lista = []
                verificante = n_numero - 1

                for i in range(n_numero):
                    prototipo = ''
                    for j in range(n_numero):
                        if j == verificante:
                            prototipo += '2'
                            verificante -= 1
                        else:
                            if j == i:
                                prototipo += '1'
                                
                            else:
                                prototipo += '3'
                    
                    lista.append(prototipo)

                for elemento in lista:
                    print(elemento)
        except EOFError:
            break
main()