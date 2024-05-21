import sys
from collections import deque
input = sys.stdin.readline

def solution(n, m, graph):
    dxdy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    answer = [[-1 for _ in range(m)] for _ in range(n)]
    q = deque()
    for i in range(n):
        for l in range(m):
            if graph[i][l] == 2:
                q.append((l, i))
                answer[i][l] = 0
            elif graph[i][l] == 0:
                answer[i][l] = 0

    while q:
        x, y = q.popleft()
        for dx, dy in dxdy:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= m or ny >= n or answer[ny][nx] != -1 or graph[ny][nx] == 0:
                continue
            answer[ny][nx] = answer[y][x] + 1
            q.append((nx, ny))

    return answer

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

arr = solution(n, m, graph)
for i in range(n):
    for l in range(m):
        print(arr[i][l], end=' ')
    print()
