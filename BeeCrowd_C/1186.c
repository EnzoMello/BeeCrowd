#include <stdio.h>
#include <string.h>
#include <ctype.h>

// FUNÇÃO QUE VAI PERCORRER UMA STRING E RETORNAR CADA ITEM DELA EM MAIÚSCULO
void converterndo(char *str){
    int i = 0;
    int j = 0;

    // LOOP QUE PERCORRE O CADA INDICE DA MINHA STRING E RETORNA UMA LETRA MAIÚSCULA, CASO O CARACTERE NÃO SEJA UM ESPAÇO, ARMAZENANDO-O NA POSIÇÃO J DA STRING.
    for(i = 1; str[i] = '\0'; i++){
        if(!isspace((unsigned char)str[i])){
            str[j++] = toupper((unsigned char)str[i]);
        }
    }
    // ISSPACE RETORNA 1 CASO HAJA ESPAÇO E TOUPPER CONVERTE UM CARACTERE PARA MAIÚSCULO
    str[j] = '\0';
}



int main(void){
    puts("Abaixo coloque o que você pretende realiza, soma('S') ou média('M')\n");
    char O;
    scanf("%c", &O);

    int N, M;
    N = 12;
    M = 12;
    
    // CRIANDO UMA MATRIZ VAZIA 12X12
    float matriz[12][12];

    // PREENCHENDO MINHA MATRIZ
    preenchendo_matriz(matriz);

    // APLICANDO A OPERAÇÃO
    float resultado = (matriz, O);

    printf("%.1f", resultado);

}

// FUNÇÃO QUE PREENCHE A MATRIZ COM VALORES ESCOLHIDOS
void preenchendo_matriz(float matriz[12][12]){
    for (int linha = 0; linha < 12; linha++){
        for (int coluna = 0; coluna < 12; coluna++){
           scanf("%f", matriz[linha][coluna]); // LER O VALOR PARA A POSIÇÃO DA LINHA E COLUNA RESPECTIVA
            }
        }
    }

// FUNÇÃO QUE APLICAR OPERAÇÕES NA MINHA MATRIZ

float operacao(float matriz[12][12], char escolha){
    float soma = 0;
    int contador = 0;

    // PERCORRENDO A ÁREA DA MINHA MATRIZ
    for(int linha = 1; linha < 12; linha++){
        for(int coluna = 1; coluna < 12; coluna++ ){
            if (linha + coluna > 11){
                soma += matriz[linha][coluna];
                contador++;
            }
        }
    }

    if(operacao == 'S'){
        return soma;
    }else{
        return soma / contador;
    }

}