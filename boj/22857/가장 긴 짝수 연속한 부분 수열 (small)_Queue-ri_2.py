import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, k = 0, 0
series, memo = [], []

def dp(i, cnt):
    global memo
    
    if cnt > k or i > n-1:
        return 0
    
    if memo[i][cnt] > 0:
        return memo[i][cnt]
        
    mx = 0
    if series[i] % 2 == 0:
        mx = max(mx, dp(i+1, cnt) + 1) # 삭제 x
    else:
        mx = max(mx, dp(i+1, cnt+1)) # 삭제 o
    
    memo[i][cnt] = mx
    return mx


def solution():
    global n, k, series, memo
    n, k = map(int, input().split())
    series = list(map(int, input().split()))
    memo = [[0 for _ in range(k+1)] for __ in range(n+1)]
    
    mx = 0
    for i in range(n):
        ret = dp(i, 0)
        mx = max(mx, ret)
        
    print(mx)
    
    
if __name__ == '__main__':
    solution()