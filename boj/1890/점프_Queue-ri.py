import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = 0
board, memo = [], []
dy = [0, 1]
dx = [1, 0]

def dfs(y, x):
    global memo
    if y == n-1 and x == n-1:
        return 1
    if ~memo[y][x]:
        return memo[y][x]
    else:
        memo[y][x] = 0
        for i in range(2):
            ny = y + dy[i] * board[y][x]
            nx = x + dx[i] * board[y][x]
            if 0 <= ny < n and 0 <= nx < n:
                memo[y][x] += dfs(ny, nx)
    return memo[y][x]
    
def solution():
    global n, board, memo
    n = int(input())
    for _ in range(n):
        board.append(list(map(int, input().split())))
    
    memo = [[-1]*n for _ in range(n)]
    print(dfs(0, 0))

if __name__ == '__main__':
    solution()