import sys
import copy
input = sys.stdin.readline

def solution(R, C, N, grid):
    if N < 2:
        return grid
    answer = [["O" for _ in range(C)] for _ in range(R)]
    prev = copy.deepcopy(grid)
    dxdy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    t = 2
    while t <= N:
        if t % 2 == 0:
            answer = [["O" for _ in range(C)] for _ in range(R)]
        else:
            for j in range(R):
                for i in range(C):
                    if prev[j][i] == "O":
                        answer[j][i] = '.'
                        for dx, dy in dxdy:
                            nx, ny = i + dx, j + dy
                            if nx < 0 or ny < 0 or nx >= C or ny >= R:
                                continue
                            answer[ny][nx] = '.'
            prev = copy.deepcopy(answer)
        t += 1

    return answer

R, C, N = map(int, input().split())
grid = [[] for _ in range(R)]
for i in range(R):
    grid[i] = list(input())
sol = solution(R, C, N, grid)
answer = ""
for i in range(R):
    for l in range(C):
        answer += str(sol[i][l])
    if i != R - 1:
        answer += '\n'
print(answer)
