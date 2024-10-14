# 구현은 매우 쉬운데 이론을 알아야 함
# https://www.acmicpc.net/board/view/141916

import sys
from math import inf
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = 0
series = []
memo = []

def solution():
    global n, series, memo
    n = int(input())
    series = list(map(int, input().split()))
    memo = [-inf for _ in range(n)]
    
    memo[0] = series[0]
    for i in range(1, n):
        memo[i] = max(memo[i-1] + series[i], series[i])
        
    print(max(memo))
        

if __name__ == '__main__':
    solution()