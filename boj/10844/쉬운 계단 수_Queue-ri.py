import sys
input = sys.stdin.readline
    
def solution():
    n = int(input())
    memo = [[0] * 10 for _ in range(n+1)]
    for i in range(1, 10):
        memo[1][i] = 1
    MOD = int(1e9)
    
    for i in range(2, n+1):
        for j in range(10):
            if j == 0:
                memo[i][j] = memo[i-1][1]
            elif j == 9:
                memo[i][j] = memo[i-1][8]
            else:
                memo[i][j] = memo[i-1][j-1] + memo[i-1][j+1] 
    
    print(sum(memo[n]) % MOD)

if __name__ == '__main__':
    solution()