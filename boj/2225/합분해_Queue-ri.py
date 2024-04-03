import sys
input = sys.stdin.readline
    
def solution():
    n, k = map(int, input().split())
    memo = [[0] * (k+1) for _ in range(n+1)]
    memo[0][0] = 1
    
    for i in range(0, n+1):
        for j in range(1, k+1):
                memo[i][j] = memo[i-1][j] + memo[i][j-1]
    
    print(memo[n][k] % int(1e9))

if __name__ == '__main__':
    solution()