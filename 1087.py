def main():
    
    while True:
        X1, Y1, X2, Y2 = input().split()

        if X1 == '0' and X2 == '0' and Y1 == '0' and Y2 == '0':
            break
        else:
            distancia_x = abs(int(X2) - int(X1))
            distancia_y = abs(int(Y2) - int(Y1))
            
            if distancia_x == 0 and distancia_y == 0:
                print("0")
            elif distancia_x == distancia_y or distancia_x == 0 or distancia_y == 0:
                print("1")
            else:
                print("2")
main()