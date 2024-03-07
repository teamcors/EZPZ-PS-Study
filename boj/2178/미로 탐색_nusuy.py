import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
maps = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    r = input()
    for j in range(m):
        maps[i][j] = int(r[j])


def solution(n, m, maps):
    answer = 0
    visited = [[False for _ in range(m)] for _ in range(n)]
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    q = deque([(0, 0)])

    while q:
        c = q.popleft()
        x = c[0]
        y = c[1]
        visited[y][x] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (
                nx < 0
                or ny < 0
                or nx >= m
                or ny >= n
                or maps[ny][nx] == 0
                or visited[ny][nx]
            ):
                continue
            visited[ny][nx] = True
            maps[ny][nx] = maps[y][x] + 1
            q.append((nx, ny))
    answer = maps[n - 1][m - 1]
    return answer


print(solution(n, m, maps))
