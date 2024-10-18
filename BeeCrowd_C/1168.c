#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// CADA DÍGITO É FORMADO POR UM 'PAUZINHO' E ELES CORRESPONDEM AO NÚMERO DE LEDS NECESSÁRIO PARA TAL DÍGITO

int main(void){
    int pauzinhos[] = {6,2, 5, 5, 4, 5, 6, 3, 7, 6,};
    int n;

    scanf("%d", &n);

    // GERA UM NOVO CASO DE TESTE PARA CADA VALOR N
    for(int i = 0; i < n; i++){
        int valorTotal = 0;
        char valor[100];
        scanf("%s", valor);

        // CADA DIGITO(STR) EM VALOR SERÁ IGUAL A UM INTEIRO EM PAUZINHOS E SERÁ INCREMENTADO ESSE VALOR EM leds_totais
        for(int i = 0; i < strlen(valor); i++){
            valorTotal += pauzinhos[valor[i] - '0']; // O - 0 É USADO PORQUE O VALOR PEGO EM C É O ASCII. DESSE MODO, O 0 FAZ A SUBTRAÇÃO E DEIXA O NÚMERO "PRONTO".
        }

        printf("%d leds\n", valorTotal);
    }

}