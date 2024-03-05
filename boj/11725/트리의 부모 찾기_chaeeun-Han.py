# 22m 35sec
import sys
sys.setrecursionlimit(10**6)

def dfs(graph, start, visited):
    visited[start] = True

    # start 외의 다른 노드가 visited가 아니라면 start is root
    for node in graph[start]:
        if not visited[node]:
            answer[node] = start
            dfs(graph, node, visited)

n = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n + 1)]
answer = [0] * (n+1)

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
dfs(graph, 1, visited)

for root in answer[2:]:
    print(root)
