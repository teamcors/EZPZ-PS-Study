import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, k = 0, 0
memo = []
MOD = int(1e9)

def dp(depth, s): # depth: 0 ~ n / s: sum
    global memo
    
    if depth == k and s == n:
        return 1
        
    if depth == k and s != n:
        return 0
        
    if s > n:
        return 0
        
    if ~memo[depth][s]:
        return memo[depth][s]
    
    res = 0
    for i in range(n+1):
        res = (res + dp(depth+1, s+i)) % MOD
    
    memo[depth][s] = res
    return res
    

def solution():
    global n, k, memo
    n, k = map(int, input().split())
    memo = [[-1] * (n+1) for _ in range(k+1)]
    
    ans = 0
    for i in range(n+1):
        ans = (ans + dp(1, i)) % MOD
    
    print(ans)
        
if __name__ == '__main__':
    solution()