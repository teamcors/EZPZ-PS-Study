import sys
from math import inf
input = sys.stdin.readline

n = 0
series, op = [], []

def dfs(result, depth):
    if depth == n:
        return result
    
    mx, mn = -inf, inf
    if op[0] > 0:
        op[0] -= 1
        a = result[0] + series[depth]
        b = result[1] + series[depth]
        k = dfs((a, b), depth + 1)
        if k[0] > mx: mx = k[0]
        if k[1] < mn: mn = k[1]
        op[0] += 1
    if op[1] > 0:
        op[1] -= 1
        a = result[0] - series[depth]
        b = result[1] - series[depth]
        k = dfs((a, b), depth + 1)
        if k[0] > mx: mx = k[0]
        if k[1] < mn: mn = k[1]
        op[1] += 1
    if op[2] > 0:
        op[2] -= 1
        a = result[0] * series[depth]
        b = result[1] * series[depth]
        k = dfs((a, b), depth + 1)
        if k[0] > mx: mx = k[0]
        if k[1] < mn: mn = k[1]
        op[2] += 1
    if op[3] > 0:
        op[3] -= 1
        a = int(result[0] / series[depth])
        b = int(result[1] / series[depth])
        k = dfs((a, b), depth + 1)
        if k[0] > mx: mx = k[0]
        if k[1] < mn: mn = k[1]
        op[3] += 1
        
    return (mx, mn)

def solution():
    global n, series, op
    n = int(input())
    series = list(map(int, input().split()))
    op = list(map(int, input().split()))
    
    mx, mn = dfs((series[0], series[0]), 1)
    print(mx)
    print(mn)
    
    
if __name__ == '__main__':
    solution()
