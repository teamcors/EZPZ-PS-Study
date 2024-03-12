from itertools import combinations
from collections import deque
import sys
import copy

input = sys.stdin.readline

n, m = map(int, input().split())
maps = []
for i in range(n):
    maps.append(list(map(int, input().split())))
dx = (-1, 0, 1, 0)
dy = (0, -1, 0, 1)


def solution(n, m, maps):
    empty = []
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0:
                empty.append((j, i))
    wall = combinations(empty, 3)
    result = 0
    for w in wall:
        q = deque()
        maps_c = copy.deepcopy(maps)
        for i in range(3):
            x, y = w[i]
            maps_c[y][x] = 1
        for i in range(n):
            for j in range(m):
                if maps[i][j] == 2:
                    q.append((j, i))
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= m or ny >= n:
                    continue
                if maps_c[ny][nx] == 0:
                    maps_c[ny][nx] = 2
                    q.append((nx, ny))

        result = max(result, find_empty(n, m, maps_c))
    return result


def find_empty(n, m, maps_cp):
    result = 0
    for i in range(n):
        for j in range(m):
            if maps_cp[i][j] == 0:
                result += 1
    return result


print(solution(n, m, maps))
