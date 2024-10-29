class casa:
    def __init__(self, lin, col):
        self.lin = lin
        self.col = col
        self.vizinhos = []
        self.ID = 8 * lin + col

    def add_vizinho(self, vizinho):
        self.vizinhos.append(vizinho)

def bfs(casa_inicial, casa_final, pai):
    visitados = set()
    fila = []
    visitados.add(casa_inicial)
    fila.append(casa_inicial)
    
    while fila:
        u = fila.pop(0)
        
        for v in u.vizinhos:
            if v not in visitados:
                fila.append(v)
                visitados.add(v)
                pai[v.ID] = u.ID
                if v.ID == casa_final.ID:
                    return True
    return False

def caminho(casas, casa_inicial, casa_final):
    pai = [-1] * 64
    # Para o cavalo, sempre existe um caminho de uma casa para qualquer outra casa
    caminho = 0
    if  casa_inicial == casa_final: 
        return caminho
    elif bfs(casa_inicial, casa_final, pai):
        u = casa_final
        while u.ID != casa_inicial.ID:
            caminho += 1
            u = casas[pai[u.ID]]
        return caminho

def cria_tabuleiro(casas):
    for i in range(64):
        lin = i // 8
        col = i % 8
        # Movimentos do cavalo
        for j in range(8):
            for k in range(8):
                # Se a casa (j, k) é uma que o cavalo pode se mover de (lin, col)
                # então adiciona (j, k) como vizinho.
                if abs(j - lin) == 2 and abs(k - col) == 1 or abs(j - lin) == 1 and abs(k - col) == 2:
                    casas[i].add_vizinho(casas[8 * j + k])

casas = [casa(i // 8, i % 8) for i in range(64)]
cria_tabuleiro(casas)
while True:
    try:
        casa_inicial_letra, casa_final_letra = input().split()        
        casa_inicial = casas[(8 - int(casa_inicial_letra[1])) * 8 + (ord(casa_inicial_letra[0]) - ord('a'))]
        casa_final = casas[(8 - int(casa_final_letra[1])) * 8 + (ord(casa_final_letra[0]) - ord('a'))]
        cam = caminho(casas, casa_inicial, casa_final)
        num_passos = max(0, cam)
        print(f'To get from {casa_inicial_letra} to {casa_final_letra} takes {num_passos} knight moves.')
    except EOFError:
        break