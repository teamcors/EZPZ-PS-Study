from collections import defaultdict, deque
import sys

input = sys.stdin.readline


def solution(n, k, x, edges):
    cities = [0] * (n + 1)
    cities[x] = 1
    q = deque([x])
    while q:
        c = q.popleft()
        for i in edges[c]:
            if cities[i] == 0:
                cities[i] = cities[c] + 1
                q.append(i)
    if k + 1 not in cities:
        print(-1)
        return
    for i, v in enumerate(cities):
        if v == k + 1:
            print(i)


n, m, k, x = map(int, input().split())
edges = defaultdict(list)
for i in range(m):
    a, b = map(int, input().split())
    edges[a].append(b)

solution(n, k, x, edges)
