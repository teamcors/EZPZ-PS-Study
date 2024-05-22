import sys
from collections import deque
input = sys.stdin.readline

def solution(M, N, graph):
    answer = 0
    dxdy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    q = deque([])

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                q.append([j, i])

    while q:
        x, y = q.popleft()
        for dx, dy in dxdy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < M and 0 <= ny < N and graph[ny][nx] == 0:
                # 토마토가 익으면 +1 -> 가장 큰 값이 정답
                graph[ny][nx] = graph[y][x] + 1
                q.append([nx, ny])

    for r in graph:
        if 0 in r:
            return -1
        answer = max(answer, max(r))

    return answer - 1

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

print(solution(M, N, graph))
