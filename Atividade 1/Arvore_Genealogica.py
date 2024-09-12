class Individuo:
    def __init__(self, nome, pai=None):
        self.nome = nome
        self.pai = pai
        self.familiar = []
        self.cor = 0 # 0 = branco, 1 = cinza, 2 = preto

    def adicionar_familiar(self, familiar):
        self.familiar.append(familiar)

    def __str__(self):
        return self.nome

    def __repr__(self):
        return self.nome

    def __eq__(self, other):
        if not isinstance(other, Individuo):
            return False
        return self.nome == other.nome

    def __hash__(self):
        return hash(self.nome)


def DFS_visit(grafo, u):
    u.cor = 1
    for v in u.familiar:
        if v.cor == 0:
            v.pai = u
            familias[0] -= 1
            DFS_visit(grafo, v)
    u.cor = 2

def DFS(grafo):
    for u in grafo.values():
        u.cor = 0
        u.pai = None
    for u in grafo.values():
        if u.cor == 0:
            DFS_visit(grafo, u)

pessoas = []
relacoes = []

M, N = map(int, input().split())

for i in range(N):
    entrada = input().split()
    relacoes.append([entrada[0], entrada[2]])
    pessoas.append(entrada[0])
    pessoas.append(entrada[2])

# Removendo duplicatas
pessoas = list(set(pessoas))

# Gerando número de famílias
familias = [len(pessoas)]

# Criando grafo
grafo = {pessoa : Individuo(pessoa) for pessoa in pessoas}

# Adicionando relações
for relacao in relacoes:
    pessoa1 = grafo[relacao[0]]
    pessoa2 = grafo[relacao[1]]
    pessoa1.adicionar_familiar(pessoa2)
    pessoa2.adicionar_familiar(pessoa1)

# Contando o número de famílias
DFS(grafo)
# Retornando o número de famílias
print(familias[0])


