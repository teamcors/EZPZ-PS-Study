import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = 0
memo = []
MOD = 10**9

def dp(d, idx): # idx번째 위치에서 숫자 d일때 탐색
    global memo
    if idx == n and 0<=d<10:
        return 1 # ok: step number
    
    if d<0 or 9<d:
        return 0
    
    if ~memo[d][idx]:
        return memo[d][idx]

    ans = (dp(d-1, idx+1) + dp(d+1, idx+1)) % MOD
    
    memo[d][idx] = ans
    return ans
    

def solution():
    global n, memo
    n = int(input())
    memo = [[-1 for _ in range(n+1)] for _ in range(10)]
    ans = 0
    for i in range(1, 10):
        ans += dp(i, 1)
        ans %= MOD
        
    print(ans)

if __name__ == '__main__':
    solution()