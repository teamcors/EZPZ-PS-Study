import sys
from collections import defaultdict

input = sys.stdin.readline
n = int(input())
maps = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    r = input()
    for j in range(n):
        maps[i][j] = int(r[j])

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
answer_dict = defaultdict(int)


def solution(n, maps):
    answer = []

    def DFS(x, y):
        maps[y][x] += 1
        count = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if maps[ny][nx] == 1:
                count += DFS(nx, ny)
        return count

    for i in range(n):
        for j in range(n):
            if maps[i][j] == 1:
                answer.append(DFS(j, i))
    answer.sort()
    print(len(answer))
    for h in answer:
        print(h)


solution(n, maps)
