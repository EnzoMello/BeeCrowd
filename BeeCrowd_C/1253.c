#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

// FUNÇÃO PARA TRANSFORMAR TODA A PALAVRA EM MAIÚSCULA
void converter(char *str){
    int i = 0;

    for(i = 0; str[i] != '\n'; i++){
        str[i] = toupper(str[i]);
        i++;
    }
}

// FUNÇÃO PARA TRANSFORMAR MINHA STRING
void transcrever_palavra(char palavra[], int intervalo, char palavra_transcrita[]){
    
    // ITERANDO SOBRE MINHA PALAVRA
    for(int i = 0; i < strlen(palavra); i++){
        char letra = palavra[i]; // PEGA A LETRA
        int valorCaractere = (int)letra; // REALIZA O CASTING E CONVERTE PARA O VALOR ASCII
        int transcrevendo = valorCaractere - intervalo; 

        // AJUSTANDO PARA CASO DE ULTRAPASSAR LETRAS MAIÚSCULAS
        if (transcrevendo < 65){
            transcrevendo = valorCaractere - intervalo + 26;
        }

        // CONVERTENDO CADA NUMERO ASCII PARA SUA RESPECTIVA LETRA
        char transcrito = (char)transcrevendo;
        // CONCATENANDO UMA STRING COM A LETRA MODIFICADA
        strncat(palavra_transcrita, &transcrito, 1);
    }

}

int main(void){
    int n;
    scanf("%d", &n);
    getchar(); // CONSOME O '\N' APÓS O NÚMERO. ALGO PARECIDO COM O USO DE SC.NEXT() NO JAVA.

    for (int i = 0; i < n; i++){
        char palavra[100];
        int numeroRef;
        char palavra_transcrita[100] = ""; // REINICIA CADA PALAVRA

        printf("Coloque palavra e número referência,respectivamente.\n");
        scanf("%s", palavra);
        scanf("%d", &numeroRef);

        // CONVERTENDO PALAVRAS PARA MAIÚSCULAS.
        converter(palavra);
        // TRANSCREVENDO CADA PALAVRA
        transcrever_palavra(palavra, numeroRef, palavra_transcrita);

        printf("%s\n", palavra_transcrita);
    }

    return 0;
}