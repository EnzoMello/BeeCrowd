#include <stdio.h>

int main(void){
    int A;
    int *B;
    int **C;
    int ***D;

    printf("Valor de A:\n");
    scanf("%d", &A);

    B = &A;
    C = &B;
    D = &C;

    int dobro = *B * 2;
    int triplo = **C * 3;
    int quadruplo = ***D * 4;

    printf("A: %d\n", A);
    printf("Dobro: %d\n", triplo);
    printf("Triplo: %d\n", triplo);
    printf("Quadruplo: %d\n", quadruplo);

}