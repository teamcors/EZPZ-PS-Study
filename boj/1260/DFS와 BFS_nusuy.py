from collections import deque

n, m, v = map(int, input().split())
nodes = [0 for _ in range(n)]
edges = [[0 for _ in range(n)] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    edges[a - 1][b - 1] = edges[b - 1][a - 1] = 1

dfs = []
bfs = []


def DFS(i):
    nodes[i] = 1
    dfs.append(i + 1)
    for j in range(n):
        if nodes[j] == 0 and edges[i][j] == 1:
            DFS(j)


def BFS(i):
    q = deque()
    q.append(i)
    nodes[i] = 1

    while q:
        c = q.popleft()
        bfs.append(c + 1)
        for j in range(n):
            if nodes[j] == 0 and edges[c][j] == 1:
                nodes[j] = 1
                q.append(j)


DFS(v - 1)
nodes = [0 for _ in range(n)]
BFS(v - 1)

print(*dfs)
print(*bfs)
