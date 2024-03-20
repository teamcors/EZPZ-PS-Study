# PyPy3 채점 기준
import sys
input = sys.stdin.readline

ans = 0
n, m = 0, 0
board = []

def dfs(depth):
    global ans, board
    
    if depth == n*m:
        ans += 1
        return
    
    y = depth // m + 1
    x = depth % m + 1
    
    if board[y-1][x] == 0 or board[y-1][x-1] == 0 or board[y][x-1] == 0:
        board[y][x] = 1
        dfs(depth + 1)
        board[y][x] = 0
    dfs(depth + 1)


def solution():
    global ans, board, n, m
    n, m = map(int, input().split())
    board = [[0 for _ in range(m+1)] for __ in range(n+1)]  
    
    dfs(0)
    print(ans)
    
if __name__ == '__main__':
    solution()