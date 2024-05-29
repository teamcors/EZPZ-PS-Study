from collections import deque
import sys
input = sys.stdin.readline

N, M, T = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

def solution(N, M, T, graph):
    dxdy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
    gram = -1

    q = deque([(1, 1)])
    while q:
        x, y = q.popleft()
        for dx, dy in dxdy:
            nx, ny = x + dx, y + dy
            if 0 < nx <= M and 0 < ny <= N and visited[ny][nx] == 0:
                if graph[ny - 1][nx - 1] == 2:
                    if gram != -1:
                        gram = min(gram,
                                   visited[y][x] + 1 + (N - ny) + (M - nx))
                    else:
                        gram = visited[y][x] + 1 + (N - ny) + (M - nx)
                elif graph[ny - 1][nx - 1] == 0:
                    visited[ny][nx] = visited[y][x] + 1
                    q.append((nx, ny))

    if 0 < gram <= T and 0 < visited[N][M] <= T:
        return min(gram, visited[N][M])
    elif gram == -1 and 0 < visited[N][M] <= T:
        return visited[N][M]
    elif 0 < gram <= T and (visited[N][M] < 1 or visited[N][M] > T):
        return gram
    else:
        return "Fail"

print(solution(N, M, T, graph))
