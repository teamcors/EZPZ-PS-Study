from collections import deque
import sys
input = sys.stdin.readline

N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

def solution(N, L, R, A):
    answer = 0
    dxdy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def bfs(r, c, visited):
        q = deque([(c, r)])
        union = [(c, r)]
        while q:
            x, y = q.popleft()
            for dx, dy in dxdy:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N and visited[ny][nx] == 0:
                    if L <= abs(A[ny][nx] - A[y][x]) <= R:
                        visited[ny][nx] = 1
                        q.append((nx, ny))
                        union.append((nx, ny))
        return union

    while True:
        visited = [[0 for _ in range(N)] for _ in range(N)]
        flag = 0
        for i in range(N):
            for j in range(N):
                if visited[i][j] == 0:
                    visited[i][j] = 1
                    union = bfs(i, j, visited)
                    if len(union) > 1:
                        flag = 1
                        pop = sum(A[y][x] for x, y in union) // len(union)
                        for x, y in union:
                            A[y][x] = pop
        if flag == 0:
            print(answer)
            break
        answer += 1

solution(N, L, R, A)
