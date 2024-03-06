# 47m 48sec
# 1. dfs 시간초과 -> PyPy3로 제출
# 2. RecursionError -> sys.setrecursionlimit(10**6) 추가
# 3. 메모리 초과(ㅇㄴ 난리남;;) -> bfs
from collections import deque
import sys
input = sys.stdin.readline
 
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)
 
def bfs(start):
    queue = deque()
    queue.append(start)
    cnt = 0
 
    visited = [False] * (n + 1)
    visited[start] = True
 
    while queue:
        v = queue.popleft()
        for node in graph[v]:
            if not visited[node]:
                visited[node] = True
                queue.append(node)
                cnt += 1
    return cnt
 
hack_cnt = []
for start in range(1, len(graph)):
    hack_cnt.append(bfs(start))
 
for i in range(len(hack_cnt)):
    if max(hack_cnt) == hack_cnt[i]:
        print(i + 1, end = " ")
