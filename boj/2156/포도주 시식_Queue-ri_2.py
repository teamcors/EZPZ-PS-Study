import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = 0
wine = []
memo = dict()

def dp(i, prev_status): # prev_status: 이전 포도주를 연속으로 선택했는가
    global memo
    
    if i > n-1:
        return 0
        
    if (i, prev_status) in memo:
        return memo[(i, prev_status)]
    
    a = 0
    b = 0
    if not prev_status:
        a = dp(i+1, True) + wine[i]
        b = dp(i+1, False)
    c = dp(i+2, False) + wine[i]
    
    memo[(i, prev_status)] = max(a, b, c)
    return memo[(i, prev_status)]
    

def solution():
    global n, wine
    n = int(input())
    for _ in range(n):
        wine.append(int(input()))
        
    print(dp(0, False))

if __name__ == '__main__':
    solution()