def bfs(capacidade, fonte, terminal, pai):
    visitados = set()
    fila = []
    visitados.add(fonte)
    fila.append(fonte)
    
    while fila:
        u = fila.pop(0)
        
        for v in range(len(capacidade)):
            if v not in visitados and capacidade[u][v] > 0:
                fila.append(v)
                visitados.add(v)
                pai[v] = u
                if v == terminal:
                    return True
    return False

def ford_fulkerson(capacidade, fonte, terminal):
    pai = [-1] * len(capacidade)
    fluxo_max = 0
    
    while bfs(capacidade, fonte, terminal, pai):
        caminho_fluxo = float("inf")
        s = terminal
        while s != fonte:
            caminho_fluxo = min(caminho_fluxo, capacidade[pai[s]][s])
            s = pai[s]
        fluxo_max += caminho_fluxo
        v = terminal
        while v != fonte:
            u = pai[v]
            capacidade[u][v] -= caminho_fluxo
            capacidade[v][u] += caminho_fluxo
            v = u
    return fluxo_max


resp = []
T = int(input())
for _ in range(T):
    # Lê a entrada
    N, M = input().split()
    N, M = int(N), int(M)
    nos = {"XS": [], "S": [], "M": [], "L": [], "XL": [], "XXL": []}
    for i in range(M):
        t1, t2 = input().split()
        nos[t1].append(i)
        nos[t2].append(i)
    # Cria a matriz de capacidade
    capacidade = [[0 for _ in range(M + 8)] for _ in range(M + 8)]
    for i in range(1, 7):
        capacidade[0][i] = N//6
        for j in [*nos.values()][i-1]:
            capacidade[i][j + 7] = 1
    for i in range(1, M + 1):
        capacidade[i + 6][M + 7] = 1
    # Calcula fluxo máximo via Ford-Fulkerson
    fluxo = ford_fulkerson(capacidade, 0, M + 7)
    # Verifica se é possível atender a demanda
    if fluxo == M:
        resp.append("YES")
    else:
        resp.append("NO")
print("\n".join(resp))