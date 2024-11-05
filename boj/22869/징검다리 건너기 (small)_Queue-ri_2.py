import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, k = 0, 0
stone, memo = [], []

def dp(prev, i):
    global memo
    
    if i == n:
        print('YES')
        exit(0)
        
    if memo[prev][i] != 'NONE':
        return memo[prev][i]
        
    for j in range(i+1, n+1):
        if (j-i)*(1+abs(stone[i]-stone[j])) <= k:
            dp(i, j)
    
    memo[prev][i] = 'NO'
    return 'NO'

def solution():
    global n, k, stone, memo
    
    n, k = map(int, input().split())
    stone = [0] + list(map(int, input().split()))
    memo = [['NONE'] * (n+1) for _  in range(n+1)]
    
    print(dp(1, 1))
    
    
if __name__ == '__main__':
    solution()