import sys
input = sys.stdin.readline

n = 0
series = []
memo = []

def dp(i):
    #print(i)
    global memo
    if i >= n-1:
        return 1
        
    if memo[i] > 0:
        return memo[i]
    
    mx = 0
    for j in range(i, n):
        if series[i] < series[j]:
            length = dp(j)
            mx = max(mx, length)
    
    memo[i] = mx + 1
    return mx + 1

def solution():
    global n, series, memo
    n = int(input())
    series = list(map(int, input().split()))
    memo = [0] * n
    
    mx = 0
    for i in range(0, n):
        #print('<----', i)
        if n-i <= mx:
            break
        ret = dp(i)
        mx = max(mx, ret)
        #print('memo:', memo)
        #print('---->', ret)
        
    print(mx)


if __name__ == '__main__':
    solution()