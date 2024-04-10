import sys
from math import inf
input = sys.stdin.readline
    
def solution():
    n = int(input())
    rocks = []
    for _ in range(n-1):
        a, b = map(int, input().split())
        rocks.append([a, b])
    k = int(input())
    
    q = [[0, 0, 1]]
    ans = inf
    while q:
        cur_idx, cur_value, cur_chance = q.pop()
        if cur_idx >= n-1:
            if cur_idx == n-1:
                ans = min(cur_value, ans)
            continue
        
        q.append([cur_idx+1, cur_value + rocks[cur_idx][0], cur_chance])
        q.append([cur_idx+2, cur_value + rocks[cur_idx][1], cur_chance])
        if cur_chance == 1:
            q.append([cur_idx+3, cur_value+k, 0])
    
    print(ans)

if __name__ == '__main__':
    solution()