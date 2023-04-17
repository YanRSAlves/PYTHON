#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <string.h>
#include <math.h>
#include <time.h>
int main()
{
	setlocale(LC_ALL,"Portuguese");

    int jogador, computador;


    //Define os números aleatórios
    srand(time(NULL));


    printf("\n\n\033[1;35m   =-=-=-=\033[m \033[1;31mJOKENPÔ\033[m \033[1;33m=-=-=-=\033[m");


    //Definindo a escolha do jogador
    printf("\n\n   1 para PEDRA\t\t\n   2 para PAPEL\t\t\n   3 para TESOURA\n\n  Sua Escolha: ");
    scanf("%d",&jogador);


    //Definindo a escolha aleatória do computador
    computador = rand()%3 + 1;

    //Caso o computador ganhe
    if (computador == 1 && jogador == 3){
        printf("\n\033[1;31m  O computador escolheu pedra e o jogador escolheu tesoura ,portanto você perdeu !!!\033[m");
    }
    else if (computador == 2 && jogador == 1){
        printf("\n\033[1;31m  O computador escolheu papel e o jogador escolheu pedra ,portanto você perdeu !!!\033[m");
    }
    else if (computador == 3 && jogador == 2){
        printf("\n\033[1;31m  O computador escolheu tesoura e o jogador escolheu papel ,portanto você perdeu !!!\033[m");
    }


    //Caso o jogador ganhe

    else if (jogador == 1 && computador == 3){
        printf("\n\033[1;32m  O computador escolheu tesoura e você deu uma pedrada na tesoura dele !!!\033[m");
    }
    else if (jogador == 2 && computador == 1){
        printf("\n\033[1;32m  O computador escolheu papel e você cortou o papel dele !!!\033[m");
    }
    else if (jogador == 3 && computador == 2){
        printf("\n\033[1;32m  O computador pedra e sufocou a pedra com o papel !!!\033[m");
    }

    //Caso o jogo der empate
    else {
        printf("\n\033[1;34m  O computador escolheu a mesma ferramenta que você !!!\033[m");
    }





    return 0;
}
