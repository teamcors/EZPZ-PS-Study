import sys
from collections import deque

input = sys.stdin.readline
N, M, K, X = map(int, input().split(' '))
graph = [[] for _ in range(N+1)]

for _ in range(M):
  a, b =  map(int, input().split(' '))  
  graph[a].append(b)

distance = [-1] *(N+1)
distance[X] = 0

# BFS
q = deque([X])
while q:
  now = q.popleft()

  for next in graph[now]:
    if distance[next] == -1:
      distance[next] = distance[now]+1
      q.append(next)

if K in distance:
  for i in range(1, N+1):
    if distance[i] == K:
      print(i)
      check = True
else:
  print(-1)
