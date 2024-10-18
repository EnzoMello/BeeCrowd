def main():
    while True:
        texto = input()
        # CONDIÇÃO DE PARADA DO MEU CÓDIGO. COMO SÃO "VÁRIAS ENTRADAS", O WHILE É UM WHILE TRUE
        if texto == 'EOF':
            break
        # SE NÃO PARA, INICIA A VERIFICAÇÃO E ALTERAÇÃO
        else:
            novo_texto = ''
            asterisco = 0
            sublinhado = 0
            # PEGO O LEN(TEXTO) E ELE VAI PULAR SOBRE CADA POSIÇÃO NO MEU INPUT, PORÉM ELE NÃO PEGA A LETRA DA POSIÇÃO EM QUE ESTÁ
            for caractere in range(len(texto)):
                # O TEXTO[CARACTERE] PEGA A LETRA CORRESPONDENTE À POSIÇÃO DO CARACTERE ATUAL E FAZ AS MODIFICAÇÕES
                if texto[caractere] == '*' and asterisco == 0:
                    asterisco += 1
                    novo_texto += '<b>'
                elif texto[caractere] == '*' and asterisco == 1:
                    novo_texto += '</b>'
                    asterisco -= 1
                else:
                    pass
                    
                if texto[caractere] == '_' and sublinhado == 0:
                    sublinhado += 1
                    novo_texto += '<i>'
                elif texto[caractere] == '_' and sublinhado == 1:
                    sublinhado -= 1
                    novo_texto += '</i>'
                else:
                    pass
                if texto[caractere] != '*' and texto[caractere] != '_':
                    novo_texto += texto[caractere]

            print(novo_texto)

main()