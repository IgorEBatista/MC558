M, N = map(int, input().split())
costa = 0
mapa = [[] for _ in range(M)]
for i in range(M):
    mapa[i] = input()
for i in range(N):
    if mapa[0][i] == '#':
        costa += 1
    if mapa[M-1][i] == '#':
        costa += 1
for i in range(1, M - 1):
    if mapa[i][0] == '#':
        costa += 1
    if mapa[i][N - 1] == '#':
        costa += 1
    for j in range(1, N - 1):
        if mapa[i][j] == '#':
            if mapa[i-1][j] == '.' or mapa[i+1][j] == '.' or mapa[i][j-1] == '.' or mapa[i][j+1] == '.':
                costa += 1
print(costa)

'''
5 5
.....
..#..
.###.
..#..
.....
'''