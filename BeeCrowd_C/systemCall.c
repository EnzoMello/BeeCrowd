#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>

// System call para abrir ou criar o arquivo com permissões de escrita
// O_CREAT: cria o arquivo se ele não existir
// O_WRONLY: abre o arquivo para escrita
// O_TRUNC: se o arquivo já existir, ele será truncado (esvaziado)

int main(){
    const char *texto = "só alegria hahaha";

    // CRIANDO O ARQUIVO, ABRINDO-O E DEIXANDO-O LIMPO PARA ESCRITA(ÚTIL EM CASO DO ARQUIVO JÁ EXISTIR)
    int arquivo = open("systemCall.txt", O_CREAT | O_WRONLY | O_TRUNC, 0644);

    // VERIFICANDO ERROS AO ABRIR ARQUIVO
    if (arquivo < 0){
        puts("Erro ao abrir o arquivo\n");
        return 1;
    }

    //VERIFICANDO ERROS AO ESCREVER NO ARQUIVO
    if(write(arquivo, texto, 18) < 0){
        puts("Erro ao abrir o arquivo");
        close(arquivo);
        return 1;
    }

    //VERIFICANDO ERROS AO FECHAR ARQUIVO
    if(close(arquivo) < 0){
        puts("Erro ao fechar arquivo");
        return 1;
    }

    return 0;
}
