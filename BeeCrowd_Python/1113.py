def verificar_ordem(x, y):
    if x < y:
        return "Crescente"
    elif x > y:
        return "Decrescente"
    else:
        return ""

def main():
    continuar = True
    while continuar:
        x, y = input().split()
        x = int(x)
        y = int(y)
        if x == y:
            continuar = False
        else:
            ordem = verificar_ordem(x, y)
            if ordem:
                print(ordem)

if __name__ == "__main__":
    main()
