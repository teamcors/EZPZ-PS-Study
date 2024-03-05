# 35m 55sec
# bfs
from collections import deque
import sys
input = sys.stdin.readline

# 도시 개수, 도로 개수, 최단 거리, 출발 도시 번호
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [0] * (n+1)
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs(start):
    answer = []
    queue = deque([start])
    visited[start] = True
    distance[start] = 0

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                distance[i] = distance[v] + 1
                if distance[i] == k:
                    answer.append(i)
    if len(answer) == 0:
        print(-1)
    else:
        answer.sort()
        for i in answer:
            print(i, end='\n')

bfs(x)
