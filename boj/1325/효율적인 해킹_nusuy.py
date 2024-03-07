from collections import deque
import sys


def BFS(n, edges):
    count = [0] * (n + 1)

    for i in range(1, n + 1):
        q = deque([i])
        visited = [False] * (n + 1)
        visited[i] = True

        while q:
            c = q.popleft()
            for e in edges[c]:
                if not visited[e]:
                    visited[e] = True
                    count[i] += 1
                    q.append(e)
    mx = max(count)
    for i, v in enumerate(count):
        if v == mx:
            print(i, end=" ")


input = sys.stdin.readline
n, m = map(int, input().split())
edges = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    edges[b].append(a)

BFS(n, edges)
