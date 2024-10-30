class MinHeap:
    def __init__(self):
        self.heap = []
        self.pos = {}

    def insert(self, key, value):
        self.heap.append((key, value))
        self.pos[key] = len(self.heap) - 1
        self._bubble_up(len(self.heap) - 1)

    def extract_min(self):
        if not self.heap:
            return None
        root = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self.pos[last[0]] = 0
            self._bubble_down(0)
        del self.pos[root[0]]
        return root

    def decrease_key(self, key, new_value):
        i = self.pos[key]
        self.heap[i] = (key, new_value)
        self._bubble_up(i)

    def _bubble_up(self, i):
        parent = (i - 1) // 2
        while i > 0 and self.heap[i][1] < self.heap[parent][1]:
            self._swap(i, parent)
            i = parent
            parent = (i - 1) // 2

    def _bubble_down(self, i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(self.heap) and self.heap[left][1] < self.heap[smallest][1]:
            smallest = left
        if right < len(self.heap) and self.heap[right][1] < self.heap[smallest][1]:
            smallest = right
        if smallest != i:
            self._swap(i, smallest)
            self._bubble_down(smallest)

    def _swap(self, i, j):
        self.pos[self.heap[i][0]], self.pos[self.heap[j][0]] = self.pos[self.heap[j][0]], self.pos[self.heap[i][0]]
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def is_empty(self):
        return len(self.heap) == 0

def AGM_Prim(G, r):
    n = len(G)
    d = [float("inf")] * n
    pai = [-1] * n
    d[r] = 0
    min_heap = MinHeap()
    for v in range(n):
        min_heap.insert(v, d[v])
    while not min_heap.is_empty():
        u, du = min_heap.extract_min()
        for v, w in G[u]:
            if v in min_heap.pos and w < d[v]:
                d[v] = w
                pai[v] = u
                min_heap.decrease_key(v, w)
    return d, pai


rodando = True
m, n = input().split()
m, n = int(m), int(n)
economia = []
while rodando:
    # Cria a lista de adjacência
    malha = [[] for _ in range(m)]
    custo_total_ini = 0
    for _ in range(n):
        x, y, dist = map(int, input().split())
        malha[x].append((y, dist))
        malha[y].append((x, dist))
        custo_total_ini += dist
    # Calcula a arvore de caminhos mínimos
    d, pais = AGM_Prim(malha, 0)
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