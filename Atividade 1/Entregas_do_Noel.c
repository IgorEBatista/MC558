#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BRANCO 1
#define CINZA 2
#define PRETO 3

typedef struct casa {
    int value;
    struct casa** vizinhos;
    int num_vizinhos;
    int cor;
    struct casa* pai;
    char* brinquedo;
} Casa;

Casa* criar_casa(int value, char* brinquedo) {
    Casa* nova_casa = (Casa*)malloc(sizeof(Casa));
    nova_casa->value = value;
    nova_casa->vizinhos = NULL;
    nova_casa->num_vizinhos = 0;
    nova_casa->cor = BRANCO;
    nova_casa->pai = NULL;
    nova_casa->brinquedo = brinquedo;
    return nova_casa;
}

void adicionar_vizinho(Casa* origem, Casa* vizinho) {
    origem->vizinhos = (Casa**)realloc(origem->vizinhos, sizeof(Casa*) * (origem->num_vizinhos + 1));
    origem->vizinhos[origem->num_vizinhos] = vizinho;
    origem->num_vizinhos++;
}

int casas_iguais(Casa* c1, Casa* c2) {
    if (c1 == NULL || c2 == NULL) {
        return (c1 == NULL && c2 == NULL);
    }
    return c1->value == c2->value;
}

Casa** encontrar_caminho(Casa* origem, Casa* destino, int* caminho_tamanho) {
    if (casas_iguais(origem, destino)) {
        Casa** caminho = (Casa**)malloc(sizeof(Casa*));
        caminho[0] = origem;
        *caminho_tamanho = 1;
        return caminho;
    } else if (destino->pai == NULL) {
        *caminho_tamanho = 0;
        return NULL;
    } else {
        int tam;
        Casa** caminho = encontrar_caminho(origem, destino->pai, &tam);
        if (caminho) {
            caminho = (Casa**)realloc(caminho, sizeof(Casa*) * (tam + 1));
            caminho[tam] = destino;
            *caminho_tamanho = tam + 1;
        }
        return caminho;
    }
}

int BFS(Casa** grafo, int tamanho, Casa* origem, Casa* destino) {
    for (int i = 0; i < tamanho; i++) {
        grafo[i]->cor = BRANCO;
        grafo[i]->pai = NULL;
    }
    origem->cor = CINZA;
    
    Casa** fila = (Casa**)malloc(tamanho * sizeof(Casa*));
    int inicio = 0, fim = 0;
    fila[fim++] = origem;
    
    while (inicio != fim) {
        Casa* atual = fila[inicio++];
        if (casas_iguais(atual, destino)) {
            free(fila);
            return 1;
        }
        for (int i = 0; i < atual->num_vizinhos; i++) {
            Casa* vizinho = atual->vizinhos[i];
            if (vizinho->cor == BRANCO) {
                vizinho->cor = CINZA;
                vizinho->pai = atual;
                fila[fim++] = vizinho;
            }
        }
        atual->cor = PRETO;
    }
    
    free(fila);
    return 0;
}

int main() {
    int N, M;
    scanf("%d %d", &N, &M);

    // Lendo os brinquedos
    char** brinquedos = (char**)malloc(N * sizeof(char*));
    for (int i = 0; i < N; i++) {
        brinquedos[i] = (char*)malloc(101 * sizeof(char));
        scanf("%s", brinquedos[i]);
    }

    // Criando as casas
    Casa** casas = (Casa**)malloc((N + 1) * sizeof(Casa*));
    for (int i = 1; i <= N; i++) {
        casas[i] = criar_casa(i, brinquedos[i - 1]);
    }

    // Lendo as conexões
    for (int i = 0; i < N - 1; i++) {
        int u, v;
        scanf("%d %d", &u, &v);
        adicionar_vizinho(casas[u], casas[v]);
        adicionar_vizinho(casas[v], casas[u]);
    }

    // Lendo as perguntas
    for (int i = 0; i < M; i++) {
        int u, v;
        scanf("%d %d", &u, &v);

        Casa* origem = casas[u];
        Casa* destino = casas[v];
        int* lista = (int*)calloc(N, sizeof(int));
        int brinquedo_unicos = 0;

        if (BFS(casas, N + 1, origem, destino)) {
            int caminho_tam;
            Casa** caminho = encontrar_caminho(origem, destino, &caminho_tam);
            if (caminho) {
                for (int j = 0; j < caminho_tam; j++) {
                    int ja_existe = 0;
                    for (int k = 0; k < brinquedo_unicos; k++) {
                        if (strcmp(lista[k], caminho[j]->brinquedo) == 0) {
                            ja_existe = 1;
                            break;
                        }
                    }
                    if (!ja_existe) {
                        lista[brinquedo_unicos++] = caminho[j]->brinquedo;
                    }
                }
                free(caminho);
            }
        }

        printf("%d\n", brinquedo_unicos);
        free(lista);
    }

    for (int i = 1; i <= N; i++) {
        free(casas[i]->vizinhos);
        free(casas[i]);
    }
    free(casas);
    for (int i = 0; i < N; i++) {
        free(brinquedos[i]);
    }
    free(brinquedos);

    return 0;
}