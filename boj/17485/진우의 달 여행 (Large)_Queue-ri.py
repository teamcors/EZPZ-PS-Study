import sys
from math import inf
input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    memo = [[[0]*3 for _ in range(m)] for __ in range(n)]
    for j in range(m):
        for k in range(3):
            memo[0][j][k] = matrix[0][j]
    
    for i in range(1, n):
        for j in range(m):
            for k in range(3):
                if (j == 0 and k == 0) or (j == m-1 and k == 2):
                    memo[i][j][k] = inf
                    continue
                if k == 0:
                    memo[i][j][k] = matrix[i][j] + min(memo[i-1][j-1][1], memo[i-1][j-1][2])
                elif k == 1:
                    memo[i][j][k] = matrix[i][j] + min(memo[i-1][j][0], memo[i-1][j][2])
                else:
                    memo[i][j][k] = matrix[i][j] + min(memo[i-1][j+1][0], memo[i-1][j+1][1])
    
    res = inf
    for j in range(m):
        res = min(res, min(memo[-1][j]))
    
    print(res)

if __name__ == '__main__':
    solution()