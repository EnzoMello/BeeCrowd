// PROGRAMA QUE FAZ O EXERCÍCIO SUB ROTINAS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void){
    // 1 QUESTAO
    float velocidade, conversao;
    puts("Coloque a velocidade em m/s abaixo\n");
    scanf("%f", &velocidade);

    conversao = velocidade * 3.6;
    printf("Velocidade em km/h: %.2f\n", conversao);

    // 2 QUESTAO
    int horas, minutos, minutosTotais;
    puts("Coloque as e os minutos, respectivamente\n");
    scanf("%d %d", &horas, &minutos);
    minutosTotais = (horas * 60) + minutos;
    printf("Minutos Totais = %d", minutosTotais);

    // 3 QUESTAO
    float dolarValor, dolar, total;
    printf("Coloque o valor em dólar e o valor do dólar\n");
    scanf("%f ", dolarValor);
    scanf("%f", dolar);
    total = dolarValor * dolar;
    printf("Total = %.2f", total);

}