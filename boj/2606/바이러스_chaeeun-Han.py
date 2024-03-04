from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n = int(input())
line = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(line):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
bfs(graph, 1, visited)
print(visited.count(True)-1)
