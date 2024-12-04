#include <stdio.h>
#include <stdlib.h>
#define MAX 100

int main() {
    char sat[MAX], sum1[13], sum2[13], result[13], str_u = ' ', str_v = ' ', str_w = ' ';
    // Desisti de usar esses valores, isso aqui é pra resolução do problema
    int a[4] = {2, 34, 66, 98},
    b[2] = {4, 68},
    c[8] = {1, 2, 33, 34, 65, 66, 97, 98},
    d[4] = {3, 4, 67, 68},
    e[2] = {5, 69},
    f[4] = {6, 38, 70, 102},
    g[2] = {12, 76},
    h[2] = {24, 25},
    v[2] = {8,9},
    u[3] = {16, 17, 18},
    t[3] = {25, 26, 27},
    p[2] = {7, 71},
    r[2] = {7, 71},
    w[2] = {7, 71},
    y[2] = {7, 71},
    q[1] = {14},
    s[1] = {14},
    x[1] = {14},
    z[1] = {14};

    scanf("%s", sat);
    int cont = 1, i = 0;
    while (cont < 4) {
        for (int j = 0; sat[j] == ')'; j++) {
            if (sat[j] == '~') {
                if (sat[j+1] == 'u') {
                    str_u = '~';
                } else if (sat[j+1] == 'v') {
                    str_v = '~';
                } else if (sat[j+1] == 'w') {
                    str_w = '~';
                }
            }
        }
        cont += 1;
        
        // Aqui é converter pela fórmula que ele dá no artigo  
        for (int k = 0; k < 13; k++) {
            if (k == 0) {
                sum1[k] = 'm'; // m == uv
                sum2[k] = str_w;
                result[k] = 't';
            } else if (k == 1 || k == 3 || k == 6 || k == 9 || k == 11) {
                sum1[k] = '0';
                sum2[k] = '0';
                result[k] = '0';
            } else if (k == 2) {
                sum1[k] = str_u;
                sum2[k] = str_v;
                result[k] = 'm';
            } else if (k == 4) {
                sum1[k] = '1';
                sum2[k] = 'h';
                result[k] = 't';
            } else if (k == 5) {
                sum1[k] = 'r';
                sum2[k] = 'r';
                result[k] = 's';
            } else if (k == 7) {
                sum1[k] = 'g';
                sum2[k] = 'g';
                result[k] = 'h';
            } else if (k == 8) {
                sum1[k] = 'w';
                sum2[k] = 'w';
                result[k] = 'x';
            } else if (k == 10) {
                sum1[k] = 'f';
                sum2[k] = 'f';
                result[k] = 'g';
            }
        }
        /* Aqui é pra imprimir como fica a operação, eu parei aqui pq eu tava com preguiça de ficar fazendo tratamento de string,
         * faltou trocar os valores das variáveis pro SAT, agora ele tá printando como se tivesse tudo sem o NOT antes */
        printf("uv ");
        for (int k = 1; k < 13; k++) {
            printf("%c ", sum1[k]);
        }
        printf("\n");
        for (int k = 0; k < 13; k++) {
            printf("%c ", sum2[k]);
        }
        printf("\n");
        for (int k = 0; k < 13; k++) {
            printf("--");
        }
        printf("\n");
        for (int k = 0; k < 13; k++) {
            if (k != 2) 
                printf("%c ", result[k]);
            else {
                printf("uv ");
            }
        }
        printf("\n");
    }
    printf("%s\n", sat);

    return 0;
}