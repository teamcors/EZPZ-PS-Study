import sys
from math import inf
input = sys.stdin.readline

n = 0
ing = []

def dfs(idx, taste):
    if idx == n:
        return taste if taste[1] else (inf, 0)
        
    res_n = dfs(idx+1, taste)
    
    sour = ing[idx][0]
    bitter = ing[idx][1]
    new_taste = (taste[0] * sour, taste[1] + bitter)
    
    res_y = dfs(idx+1, new_taste)
    
    val_n = abs(res_n[0] - res_n[1])
    val_y = abs(res_y[0] - res_y[1])
    
    return res_n if val_n < val_y else res_y

def solution():
    global n, ing
    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())
        ing.append((a, b))
        
    best = dfs(0, (1,0))
    print(abs(best[0]-best[1]))
    
if __name__ == '__main__':
    solution()
