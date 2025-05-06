direções = [(1, 0), (0, -1), (-1, 0), (0, 1)]  

N, M, K = map(int, input().split())

# Posições e direções iniciais dos aviões
avioes = []
for _ in range(N):
    X,Y = map(int, input().split())
    avioes.append({'x': X, 'y': Y, 'dir': 0})  # direção inicial: Este

# Conjunto com posições das nuvens
nuvens = set()
for _ in range(M):
    X,Y = map(int, input().split())
    nuvens.add((X, Y))

# Histórico de posições visitadas por cada avião
historico = [set() for _ in range(N)]

# Adicionar posição inicial ao histórico
for i in range(N):
    historico[i].add((avioes[i]['x'], avioes[i]['y']))

# Simular o movimento durante K unidades de tempo
for _ in range(K):
    for i in range(N):
        dx, dy = direções[avioes[i]['dir']]
        nx = avioes[i]['x'] + dx
        ny = avioes[i]['y'] + dy

        if (nx, ny) in nuvens:
            # Colidiu com nuvem → vira à direita
            avioes[i]['dir'] = (avioes[i]['dir'] + 1) % 4
        else:
            # Move-se normalmente
            avioes[i]['x'] = nx
            avioes[i]['y'] = ny
            historico[i].add((nx, ny))

# Contar pares de aviões que se cruzaram (pelo menos uma posição em comum)
pares = set()
for i in range(N):
    for j in range(i + 1, N):
        if historico[i].intersection(historico[j]):
            pares.add((i, j))

print(len(pares))
