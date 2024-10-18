#include <stdio.h>
#include <string.h>
#include <ctype.h>

// FUNÇÃO PARA CONVERTER PARA MAIÚSCULA E REMOVER ESPAÇOS
void convertendo(char *str){
    int i = 0;
    int j = 0;

    // LOOP QUE PERCORRE O CADA INDICE DA MINHA STRING E RETORNA UMA LETRA MAIÚSCULA, CASO O CARACTERE NÃO SEJA UM ESPAÇO, ARMAZENANDO-O NA POSIÇÃO J DA STRING.
    for(i = 1; str[i] != '\0'; i++){
        if(!isspace((unsigned char)str[i])){
            str[j++] = toupper((unsigned char)str[i]);
        }
    }
    // ISSPACE RETORNA 1 CASO HAJA ESPAÇO E TOUPPER CONVERTE UM CARACTERE PARA MAIÚSCULO
    str[j] = '\0';
}


int main(void){
    char A[100];
    char B[100];

    // LENDO AS DUAS STRINGS, USANDO O SIZEOF PARA GARANTIR QUE NÃO PASSEM DOS LIMITES ESTABELECIDOS E USANDO O STDIN PARA INDICAR A REFERÊNCIA DE ONDE O PROGRAMA PEGA OS VALORES
    printf("Digite string A: ");
    fgets(A, sizeof(A), stdin);
    printf("Digite uma string B: ");
    fgets(B, sizeof(B), stdin);

    convertendo(A);
    convertendo(B);

    int count = 0;

    // VERIFICANDO AS SEQUÊNCIAS DE LETRAS IGUAIS
    for (int i = 0; i < strlen(A); i++){
        for (int j = 0; j < strlen(B); j++){
            if(B[j] == A[i]){
                count++;
                break;
            }
        }
    }

    printf("Count = %d\n", count);

}