n = int(input())
m = int(input())
nodes = [0 for _ in range(n)]
edges = [[0 for _ in range(n)] for __ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    edges[a - 1][b - 1] = edges[b - 1][a - 1] = 1


def DFS(node):
    v = 0
    nodes[node] = 1
    for l in range(n):
        if nodes[l] == 0 and edges[node][l] == 1:
            nodes[l] = 1
            v += 1
            v += DFS(l)
    return v


result = 0
for i in range(n):
    if nodes[i] == 0 and edges[0][i] == 1:
        result += DFS(i)

print(result)
