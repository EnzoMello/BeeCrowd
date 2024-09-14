# N = Número de palavras
# L = Número de linhas 
# C = Número de caracteres por linha

def main():
    while True:
        entrada = input().split()
        n_palavras = input()
        N = int(entrada[0])
        L = int(entrada[1])
        C = int(entrada[2])
        novo_texto = ''
        count_caracteres = 0
        # O LIVRO JÁ COMEÇARIA AUTOMATICAMENTE NA PRIMEIRA LINHA
        count_linhas = 1
        count_pags = 1
        
        for letra in n_palavras:
            # VERIFICANDO SE AINDA CABEM CARACTERES NA LINHA
            if count_caracteres < C:
                count_caracteres += 1
            # RESETANDO CARACTERES E AUMENTANDO LINHAS USADAS, CASO NÃO TENHA MAIS ESPAÇO PARA CARACTERES NA LINHA
            elif count_caracteres >= C:
                count_caracteres = 0
                count_linhas += 1
            # RESETANDO LINHAS E AUMENTANDO PÁGS USADAS, CASO NÃO TENHA MAIS ESPAÇO PARA LINHAS NA PÁGINA
            if count_linhas == L:
                count_pags += 1
                count_linhas = 0
        
        print(count_pags)
main()