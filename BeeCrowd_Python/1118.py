def main():
    # QUANTIDADE NOTAS É = 2 E VALIDADE DO PROGRAMA = 1
    validade = 1
    X = 0
    nota_do_aluno = 0

    while X < 3 and validade == 1 :
        nova_nota = float(input(" "))
        X += 1
        nota_do_aluno += nova_nota

        if nova_nota < 0 or nova_nota > 10:
            print("nota inválida")

            
        if X == 2:
            media = nota_do_aluno / 2
            print("media = {:.2f}".format(media))
            novo_calculo = int(input("novo calculo (1-sim 2-nao)"))

    
            while novo_calculo < 1 or novo_calculo > 2:
                novo_calculo = int(input("novo calculo (1-sim 2-nao)"))

            if novo_calculo == 1:
                X = 0
                nota_do_aluno = 0

            elif novo_calculo == 2:
                X = 3 
                validade = 2



main()