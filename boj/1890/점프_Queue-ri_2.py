import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = 0
board = []
memo = []

def dp(y, x):
    global memo
    
    if y == n-1 and x == n-1:
        return 1
        
    if ~memo[y][x]:
        return memo[y][x]
      
    memo[y][x] = 0 # visited
    k = board[y][x]
    ny = y + k
    nx = x + k
    
    ans = 0
    if ny < n: ans += dp(ny, x)
    if nx < n: ans += dp(y, nx)
    
    memo[y][x] += ans
    return ans

def solution():
    global n, board, memo
    n = int(input())
    for _ in range(n):
        board.append(list(map(int, input().split())))
        
    memo = [[-1 for _ in range(n)] for __ in range(n)]
        
    print(dp(0, 0))
    

if __name__ == '__main__':
    solution()