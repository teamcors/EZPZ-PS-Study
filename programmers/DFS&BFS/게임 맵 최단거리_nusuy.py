from collections import deque


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[0 for _ in range(m)] for __ in range(n)]
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    x = y = nx = ny = 0

    # BFS
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1

    while len(q):
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (
                nx < 0
                or ny < 0
                or nx >= len(maps[0])
                or ny >= len(maps)
                or maps[ny][nx] == 0
            ):
                continue
            if visited[ny][nx] == 0:
                visited[ny][nx] = 1
                maps[ny][nx] = maps[y][x] + 1
                q.append((ny, nx))

    if maps[n - 1][m - 1] == 1:
        return -1

    return maps[n - 1][m - 1]
