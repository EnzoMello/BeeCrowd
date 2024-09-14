def determinar_quadrante(x, y):
    quadrante = ""
    if x > 0 and y > 0:
        quadrante = "primeiro"
    if x < 0 and y > 0:
        quadrante = "segundo"
    if x < 0 and y < 0:
        quadrante = "terceiro"
    if x > 0 and y < 0:
        quadrante = "quarto"
    return quadrante

def main():
    continuar = True
    while continuar:
        entrada = input().split()
        x = int(entrada[0])
        y = int(entrada[1])
        if x == 0 or y == 0:
            continuar = False
        else:
            quadrante = determinar_quadrante(x, y)
            if quadrante != "":
                print(quadrante)

if __name__ == "__main__":
    main()
