# PRECISO FAZER UM WHILE INFINITO;PRINTAR LINHA EM BRANCO NO CASO DE NOVA RODADA;PEGA UMA LINHA DE REF. EM CADA RODADA E COMPARAR COM AS OUTRAS LINHAS NA RODADA,PARA SABER QNTS ESPAÇOS PRECISO
# LISTA PARA IR ADICIONANDO STRINGS E, AO ADICIONAR STRINGS , USAR PODER DO JOIN E SPLIT

def main():
    validade_da_rodada = 0

    while True:
        numero_de_linhas = int(input(""))
        
        # NÚMERO DE LINHAS = 0 IRÁ PARAR MEU PROGRAMA,JÁ QUE NÃO EXISTE MAIS RODADAS
        if numero_de_linhas == 0:
            break

        # VALIDADE DA RODADA = 1,PRINTA UMA LINHA EM BRANCO PARA SEPARAR AS RODADAS.ALIÁS, COMEÇA EM ZERO PORQUE ANTES DA 1 RODADA NÃO TEM NADA
        if validade_da_rodada == 1:
            print()


        minha_frase = []
        
        # CRIO UMA LISTA QUE SERÁ ADICIONADA COM UMA STRING DEDICADA PARA CADA LINHA DE NMR DE LINHAS. O JOIN JÁ ADICIONA CADA LINHA COM UM ESPAÇO ENTRE AS PALAVRAS E APPEND ADICIONA CADA LINHA NO FINAL
        for linha in range(numero_de_linhas):
            minha_frase.append(''.join(input().split()))


        # PEGO A LINHA MÁXIMA DA MINHA LISTA,PARA COMPARAR COM CADA LINHA E DEFINIR QUANTOS ESPAÇOS PRECISO
        referencia = max(len(minha_frase) for linha in minha_frase)

        # EM CADA LINHA DA MINHA LISTA, ADICIONO ESPAÇOS DE ACORDO COM A MAIOR LINHA - A LINHA ATUAL E PRINTO A LINHA ATUAL. ISSO SERVE PARA ALINHAR À DIREITA.
        for linha in range(len(minha_frase)):
            for trecho in range(referencia - len(minha_frase[linha])):
                print('',end = ' ')

                print(minha_frase[linha])

        # VALIDADE = 1 PARA TER LINHAS EM BRANCO DURANTE O LOOP
        validade_da_rodada = 1
main()