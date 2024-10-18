#include <stdio.h>
#include <stdlib.h>

int main(void){
    int vect[10];

    for(int i = 0; i < 10; i++){
        int valor;
        printf("Digite o valor da posição %d\n", i);
        scanf("%d", &valor);
        vect[i] = valor;
    }

    for(int i = 0; i < 10; i++){
        int *p;
        p = &vect[i];
        printf("Valor: %d\n", *p);
        printf("Valor do endereço: %p\n",p);

    }
    return 0;
}