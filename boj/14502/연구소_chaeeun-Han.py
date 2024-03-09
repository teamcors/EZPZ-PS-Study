# 해설 참고 함
# 48min
# == 이랑 = 오타 주의!!
from collections import deque
import sys
import copy
input = sys.stdin.readline

def bfs():
    queue = deque()
    # 바이러스의 좌표를 queue에 append
    temp_map = copy.deepcopy(map)
    for i in range(n):
        for j in range(m):
            if temp_map[i][j] == 2:
                queue.append((i, j))

    while queue:
        # 바이러스 좌표
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # nx와 ny가 내부에 있고
            if (0 <= nx < n) and (0 <= ny < m):
                # 뚫린 공간이라면
                if temp_map[nx][ny] == 0:
                    temp_map[nx][ny] = 2  # 바이러스 확산
                    queue.append((nx, ny))  # queue에 append

    global result
    count = 0
    for i in range(n):
        count += temp_map[i].count(0)

    result = max(result, count)

def make_wall(count):
    if count == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if map[i][j] == 0:
                map[i][j] = 1
                make_wall(count+1)
                map[i][j] = 0

n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]

result = 0
# 동, 서, 남, 북
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
make_wall(0)

print(result)
