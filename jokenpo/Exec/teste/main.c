#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Estrutura para armazenar os dados de cada pizza
typedef struct {
    int codigo;
    char nome[50];
    float preco;
} Pizza;

// Estrutura para armazenar os dados de cada pedido
typedef struct {
    int codigo;
    Pizza pizza;
    int quantidade;
    float valor_total;
    char forma_pagamento[20];
    char endereco_entrega[100];
} Pedido;

// Array para armazenar as pizzas disponíveis no cardápio
Pizza cardapio[10] = {
    {1, "Pizza de Mussarela", 25.00},
    {2, "Pizza de Calabresa", 28.00},
    {3, "Pizza de Frango com Catupiry", 30.00},
    {4, "Pizza de Portuguesa", 32.00},
    {5, "Pizza de Quatro Queijos", 35.00},
    {6, "Pizza de Bacon", 30.00},
    {7, "Pizza de Banana com Canela", 28.00},
    {8, "Pizza de Chocolate com Morango", 35.00},
    {9, "Pizza de Palmito", 32.00},
    {10, "Pizza de Camarão", 40.00}
};

// Array para armazenar os pedidos registrados
Pedido pedidos[100];
int num_pedidos = 0;

// Função para exibir o cardápio
void exibir_cardapio() {
    printf("------ Cardapio ------\n");
    printf("Codigo | Nome da Pizza                | Preco\n");
    printf("-------|------------------------------|------\n");
    for(int i=0; i<10; i++) {
        printf("%-6d | %-28s | R$%.2f\n", cardapio[i].codigo, cardapio[i].nome, cardapio[i].preco);
    }
    printf("----------------------\n");
}

// Função para adicionar uma nova pizza ao cardápio
void adicionar_pizza() {
    int codigo;
    char nome[50];
    float preco;

    printf("Digite o codigo da pizza: ");
    scanf("%d", &codigo);

    printf("Digite o nome da pizza: ");
    scanf(" %[^\n]s", nome);

    printf("Digite o preco da pizza: ");
    scanf("%f", &preco);


    nova_pizza = {codigo, nome, preco};
    Pizza = nova_pizza
    cardapio[codigo-1] = nova_pizza;

    printf("Pizza adicionada com sucesso!\n");
}

// Função para remover uma pizza do cardápio
void remover_pizza() {
    int codigo;

    printf("Digite o codigo da pizza que deseja remover: ");
    scanf("%d", &codigo);

    for(int i=0; i<10; i++) {
        if(cardapio[i].codigo == codigo) {
            Pizza pizza_vazia = {0, "", 0};
            cardapio[i] = pizza_vazia;
            printf("Pizza removida com sucesso!\n");
            return;
        }
    }
    printf("Nao foi encontrada nenhuma pizza com esse codigo.\n");
}

// Função para registrar um novo pedido
void registrar_pedido() {
    int codigo;
    int quantidade;
    char forma_pagamento
