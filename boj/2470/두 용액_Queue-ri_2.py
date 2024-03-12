import sys
from math import inf
input = sys.stdin.readline

def solution():
    n = int(input())
    data = sorted(list(map(int, input().split())))
    
    l, r = 0, n-1
    res = inf
    ans = (-1, -1)
    while l < r:
        new_res = data[l] + data[r]
        if abs(new_res) < res:
            res = abs(new_res)
            ans = (data[l], data[r])
            if new_res == 0:
                break
        
        if new_res < 0:
            l = l+1
        else:
            r = r-1
    
    print(*ans)

if __name__ == '__main__':
    solution()
