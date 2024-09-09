class casa:
    def __init__(self, value, brinquedo):
        self.value = value
        self.vizinhos = []
        self.cor = 1 # 1 = branco, 2 = cinza, 3 = preto
        self.pai = None
        self.brinquedo = brinquedo

    def add_vizinho(self, vizinho):
        self.vizinhos.append(vizinho)

    def __str__(self):
        return f"Casa {self.value} com brinquedo {self.brinquedo} e pai {self.pai.value if self.pai else None}"
    
    def __eq__(self, other):        
        if (self is None) or (other is None):
            if (self is None) and (other is None):
                return True
            else:
                return False 
        return self.value == other.value

def encontrar_caminho(origem : casa, destino : casa):
    if origem == destino:
        return [origem]
    elif destino.pai == None:
        return []
    else:
        caminho = encontrar_caminho(origem, destino.pai)
        if caminho:
            caminho.append(destino)
        return caminho

def BFS(grafo : list, origem : casa, destino : casa):
    for casa in grafo:
        casa.cor = 1
        casa.pai = None
    origem.cor = 2
    fila = []
    fila.append(origem)
    while fila:
        casa_atual = fila.pop(0)
        if casa_atual == destino:
            return True
        for vizinho in casa_atual.vizinhos:
            if vizinho.cor == 1:
                vizinho.cor = 2
                vizinho.pai = casa_atual
                fila.append(vizinho)
        casa_atual.cor = 3
    return False
    



# Lendo N e M
N, M = input().split()
N = int(N)
M = int(M)

# Lendo os presentes
presentes = input().split()

# Criando as casas
casas = [casa(0, 0)]
for i in range(1, N + 1):
    nova_casa = casa(i, presentes[i - 1])
    casas.append(nova_casa)

# Lendo as conexões
for i in range(N-1):
    u, v = input().split()
    u = int(u)
    v = int(v)
    casas[u].add_vizinho(casas[v])
    casas[v].add_vizinho(casas[u])
    
# Lendo as perguntas
perguntas = []
for i in range(M):
    u, v = input().split()
    u = int(u)
    v = int(v)
    perguntas.append([u, v])

# Resolvendo as perguntas
for pergunta in perguntas:
    lista = []
    origem = casas[pergunta[0]]
    destino = casas[pergunta[1]]
    if BFS(casas, origem, destino):
        caminho = encontrar_caminho(origem, destino)
        if caminho:
            for casa in caminho:
                if casa.brinquedo not in lista:
                    lista.append(casa.brinquedo)
    print(len(lista))

