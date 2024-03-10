# 35min 53sec
# 1. 틀렸습니다 
# -> 출력할 때 flooding만 이중 for문으로 출력했는데, graph가 0일 때는 graph에서 출력해야함 
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
flooding = [[-1] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(a, b):
    queue = deque()
    queue.append((a, b))

    flooding[a][b] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 내에서 아직 안 간 땅이면
            if 0 <= nx < n and 0 <= ny < m and flooding[nx][ny] == -1:
                if graph[nx][ny] == 0:  # 벽일 때
                    flooding[nx][ny] = 0
                elif graph[nx][ny] == 1:  # 갈 수 있을 때
                    flooding[nx][ny] = flooding[x][y] + 1
                    queue.append((nx, ny))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2 and flooding[i][j] == -1:
            bfs(i, j)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(0, end=' ')
        else:
            print(flooding[i][j], end=' ')
    print()
