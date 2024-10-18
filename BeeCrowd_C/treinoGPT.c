#include <stdio.h>
#include <stdlib.h>

int main(void){
    int N, M;

    //LENDO NÚMERO DE LINHAS E COLUNAS
    printf("Coloque o número de linhas(N) e colunas(M),respectivamente.\n");
    scanf("%d", &N);
    scanf("%d", &M);

    //ALOCANDO MEMÓRIA PARA AS MATRIZES
    float *A = (float *)malloc(N * M * sizeof(float));
    float *B = (float *)malloc(N * M * sizeof(float));
    float *C = (float *)malloc(N * M * sizeof(float));

    // LER AS MATRIZES A E B
    printf("Digite os elementos das matrizes %dx%d\n", N, M);
    for(int i = 0; i < N * M; i++){
        scanf("%f", (A + i)); // O X + i É UM TRUQUE ARITMÉTICO PARA MOVER UM PONTEIRO PELAS POSIÇÕES DA MATRIZ E APONTAR TAL NÚMERO PARA A POSIÇÃO
    }

    for(int i = 0; i < N * M; i++){
        scanf("%f", (B + i)); // O X + i É UM TRUQUE ARITMÉTICO PARA MOVER UM PONTEIRO PELAS POSIÇÕES DA MATRIZ E APONTAR TAL NÚMERO PARA A POSIÇÃO
    }

    // SOMANDO AS MATRIZES E ARMAZENANDO CADA RESULTADO NUMA MATRIZ C
    for(int i = 0; i < N * M; i++){
        *(C + i) = *(A + i) + *(B + i); // CADA POSIÇÃO i É USADA PARA OS PONTEIROS A E B APONTAREM PARA DIFERENTES POSIÇÕES E SOMAREM, ALOCANDO NA POSIÇÃO i DE C
    }

    // EXIBINDO O RESULTADO DA MATRIZ C
    for(int i = 0; i < N; i++){
        for (int j = 0; j < M; j++){
            printf("%.1f ", *(C + i * M + j));
        }
        printf("\n");
        }

    // LIBERANDO MEMÓRIA ALOCADA
    free(A);
    free(B);
    free(C);
        
    return 0;
    }


