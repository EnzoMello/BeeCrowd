#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* N = Número de palavras
 L = Número de linhas 
 C = Número de caracteres por linha */

 int main(void){
    int N, L, C;
    char entrada[100];
    char frase[100];
    int countCaracteres = 0;
    int countLinhas = 1;
    int countPags = 1;

    fgets(entrada, sizeof(entrada), stdin);

    //SSCANF SERVE PARA QUEBRAR UMA LINHA E ATRIBUIR VALORES A VARIAVEIS, COMO OCORRE COM O SPLIT NO PYTHON
    sscanf(entrada, "%d %d %d", &N, &L, &C);

    // LENDO A FRASE
    fgets(frase, sizeof(frase), stdin);

    for(int i = 0; i < strlen(frase); i++){
        // VERIFICANDO SE AINDA CABEM CARACTERES NA LINHA
        if (countCaracteres < C){
            countCaracteres++;
        }else{
            countCaracteres = 0;
            countLinhas++;
        }

        // RESETANDO LINHAS E AUMENTANDO PÁGS USADAS, CASO NÃO TENHA MAIS ESPAÇO PARA LINHAS NA PÁGINA
        if (countLinhas >= L){
            countLinhas = 0;
            countPags++;
        }
        
    }
    printf("%d",countPags);
    return 0;
 }