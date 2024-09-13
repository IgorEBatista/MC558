T = int(input())
movimentos = []
for i in range(T):
    contagem = 0
    N = int(input())
    V, A = map(int, input().split())
    labirinto = [[] for _ in range(V)]
    for j in range(A):
        x, y = map(int, input().split())
        labirinto[x].append(y)
        if x not in labirinto[y]:    
            labirinto[y].append(x)
            contagem += 2
    movimentos.append(contagem)

for i in movimentos:
    print(i)
