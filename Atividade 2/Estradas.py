class min_heap:
    def __init__(self):
        self.heap = []
        self.pos = {}
    
    def empty(self):
        return len(self.heap) == 0
    
    def insert(self, v, d):
        self.heap.append((v, d))
        self.pos[v] = len(self.heap) - 1
        self.up(len(self.heap) - 1)
    
    def up(self, i):
        while i > 0:
            pai = (i - 1) // 2
            if self.heap[pai][1] > self.heap[i][1]:
                self.heap[pai], self.heap[i] = self.heap[i], self.heap[pai]
                self.pos[self.heap[pai][0]] = pai
                self.pos[self.heap[i][0]] = i
                i = pai
            else:
                break
    
    def down(self, i):
        while 2 * i + 1 < len(self.heap):
            filho = 2 * i + 1
            if filho + 1 < len(self.heap) and self.heap[filho + 1][1] < self.heap[filho][1]:
                filho += 1
            if self.heap[i][1] > self.heap[filho][1]:
                self.heap[i], self.heap[filho] = self.heap[filho], self.heap[i]
                self.pos[self.heap[i][0]] = i
                self.pos[self.heap[filho][0]] = filho
                i = filho
            else:
                break
    
    def decrease_key(self, v, d):
        i = self.pos[v]
        self.heap[i] = (v, d)
        self.up(i)
    
    def increase_key(self, v, d):
        i = self.pos[v]
        self.heap[i] = (v, d)
        self.down(i)

    def extract_min(self):
        if self.empty():
            return None
        v, d = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.pos[self.heap[0][0]] = 0
        self.heap.pop()
        self.down(0)
        return v, d


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
    # Verifica o próximo caso
    m, n = input().split()
    m, n = int(m), int(n)
    if m == 0 and n == 0:
        rodando = False
print("\n".join(map(str, economia)))