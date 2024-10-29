def AGM_Prim(G, w, r):
    n = len(G)
    d = [float("inf") for _ in range(n)]
    pai = [-1 for _ in range(n)]
    d[r] = 0
    Q = set(range(n))
    while Q:
        u = min(Q, key=lambda x: d[x])
        Q.remove(u)
        for v in range(n):
            if v in Q and w[u][v] < d[v]:
                pai[v] = u
                d[v] = w[u][v]
    return d, pai

rodando = True
m, n = input().split()
m, n = int(m), int(n)
economia = []
while rodando:
    # Cria a matriz de distâncias
    malha = [[float("inf") for _ in range(m)] for _ in range(m)]
    for _ in range(n):
        x, y, dist = input().split()
        x, y, dist = int(x), int(y), int(dist)
        malha[x][y] = dist
        malha[y][x] = dist
    # Calcula a arvore de caminhos mínimos
    d, pais = AGM_Prim(malha, malha, 0)
    # Calcula o custo total inicial
    custo_total_ini = 0
    for i in range(m):
        for j in range(i + 1, m):
            if malha[i][j] != float("inf"):
                custo_total_ini += malha[i][j]
    # Calcula o custo total final
    custo_total_fim = 0
    for i in range(m):
        custo_total_fim += d[i]
    # Calcula a economia
    economia.append(custo_total_ini - custo_total_fim)
    print(custo_total_ini, custo_total_fim)
    print(d)
    print(pais)
    # Verifica o próximo caso
    m, n = input().split()
    m, n = int(m), int(n)
    if m == 0 and n == 0:
        rodando = False
print("\n".join(map(str, economia)))