import sys
from collections import deque
input = sys.stdin.readline

def solution(M, N, H, graph):
    answer = 0
    dxdydz = [(1, 0, 0), (-1, 0, 0), (0, 1, 0),
              (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    q = deque([])
    for i in range(H):
        for l in range(N):
            for k in range(M):
                if graph[i][l][k] == 1:
                    q.append((k, l, i))

    while q:
        x, y, z = q.popleft()
        for dx, dy, dz in dxdydz:
            nx, ny, nz = x + dx, y + dy, z + dz
            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H and graph[nz][ny][nx] == 0:
                graph[nz][ny][nx] = graph[z][y][x] + 1
                q.append((nx, ny, nz))

    for i in range(H):
        for l in range(N):
            if 0 in graph[i][l]:
                return -1
            answer = max(answer, max(graph[i][l]))

    if answer == 1:
        return 0

    return answer - 1

M, N, H = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

print(solution(M, N, H, graph))
