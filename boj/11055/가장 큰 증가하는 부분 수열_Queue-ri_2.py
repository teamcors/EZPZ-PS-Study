import sys
input = sys.stdin.readline

n = 0
series = []
memo = []

def dp(i):
    global memo
    if i >= n-1:
        return series[i]
        
    if memo[i] > 0:
        return memo[i]
        
    mx = 0
    for j in range(i, n):
        if series[i] < series[j]:
            ret = dp(j)
            mx = max(mx, ret)
        
    memo[i] = mx + series[i]
    return mx + series[i]
    

def solution():
    global n, series, memo
    n = int(input())
    series = list(map(int, input().split()))
    memo = [0] * n
    
    mx = 0
    for i in range(n):
        ret = dp(i)
        mx = max(mx, ret)
        
    print(mx)
    

if __name__ == '__main__':
    solution()