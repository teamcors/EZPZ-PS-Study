import sys
from math import inf
input = sys.stdin.readline

def solution():
    n = int(input())
    data = sorted(list(map(int, input().split())))
    
    best_res = inf
    ans = ()
    for i in range(n-1):
        data_i = data[i]
        # search range: i+1 ~ n-1
        mn, mx = i+1, n-1
        while mn <= mx:
            md = (mn + mx) // 2
            res = abs(data[i] + data[md])
            
            if res < best_res:
                best_res = res
                ans = (data[i], data[md])
                
            if data_i + data[md] == 0:
                break
            elif data_i + data[md] < 0:
                mn = md + 1
            else:
                mx = md - 1
        
    print(*ans)

if __name__ == '__main__':
    solution()
