def main():
    # QUANTIDADE N DE ENTRADAS QUE O USUÁRIO IRÁ FAZER
    n_entradas = int(input())

    for entrada in range(n_entradas):
        texto = input("")

        # CHAMO FUNÇÃO DA PRIMEIRA PASSADA
        texto = desloca_para_direita(texto)

        # CHAMO A FUNÇÃO DA SEGUNDA PASSADA
        texto = inverter_texto(texto)

        # CHAMO A FUNÇÃO DA TERCEIRA PASSADA
        texto = metade_para_esquerda(texto)

        print(texto)

def desloca_para_direita(texto_original):
    novo_texto = ''

    # VERIFICANDO SE É LETRA QUE É O CARACTERE ATUAL E,CASO SEJA,DESLOCANDO-A 3 CASAS NA TABELA ASCII
    for letra in texto_original:
        if (ord(letra) > 64 and ord(letra) < 91) or (ord(letra) > 96 and ord(letra) < 123):
            novo_texto += chr(ord(letra) + 3)
        else:
            novo_texto += letra
        
    # RETORNO O TEXTO ANALISADO E DESLOCADO PARA DIREITA,DE ACORDO COM TABELA ASCII
    return novo_texto

# INVERTENDO O TEXTO. A INVERSÃO É POSSIBILITADA PELO -1,QUE PERCORRE O TEXTO AO CONTRÁRIO 
# NOTE QUE O RETURN JÁ RETORNA A PALAVRA COM AS LETRAS INVERTIDAS,SEM GASTAR LINHAS CRIANDO OUTRAS VARIÁVEIS
def inverter_texto(exemplo):
    return exemplo[::-1]


def metade_para_esquerda(texto_original):
    texto_modificado = ''

    # PEGO O TAMANHO DO TEXTO E DIVIDO ESSE TAMANHO AO MEIO
    metade = len(texto_original) // 2

    # PEGO APENAS A METADE PARA DIREITA DO MEU TEXTO E DESLOCO CADA LETRA PARA A ESQUERDA,SEGUNDO TABELA ASCII
    for caractere in texto_original[metade::]:
        texto_modificado += chr(ord(caractere) - 1)

    # PEGO A METADE DA ESQUERDA DO TEXTO E ACRESCENTADO A PARTE DA DIREITA,QUE FOI MODIFICADA.
    return texto_original[:metade] + texto_modificado

main()