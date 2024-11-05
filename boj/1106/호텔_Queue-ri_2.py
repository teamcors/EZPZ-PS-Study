import sys
from math import ceil
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

c, n = 0, 0
data, memo = [], []
inf = 1987654321

def dp(city, remain):
    global memo
    
    if city >= n and remain > 0:
        return inf
    
    if remain <= 0:
        return 0
    
    if memo[city][remain] > 0:
        return memo[city][remain]
    
    mn = inf
    KMAX = ceil(remain / data[city][1])
    
    for k in range(KMAX+1):
        new_remain = remain - data[city][1] * k
        ret = dp(city+1, new_remain) + data[city][0] * k
        if ret < mn: mn = ret
        
    memo[city][remain] = mn
    return mn
    

def solution():
    global c, n, data, memo
    
    c, n = map(int, input().split())
    data = [0] * n
    for i in range(n):
        pay, people = map(int, input().split())
        data[i] = (pay, people)
        
    memo = [[0] * (c+101) for _ in range(n)]
    
    # c를 넘어가더라도 더 가성비있을 수 있으므로 c+100까지 탐색
    mn = inf
    for i in range(101):
        ret = dp(0, c+i)
        if ret < mn: mn = ret # min( dp(0, c) ~ dp(0, c+100) )
    print(mn)
    
if __name__ == '__main__':
    solution()