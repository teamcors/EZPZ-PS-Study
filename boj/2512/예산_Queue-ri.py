import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    req = list(map(int, input().split()))
    m = int(input())
    
    mn, mx = 0, m
    ans = 0
    while mn <= mx:
        md = int((mn+mx)/2)
        used = 0
        for r in req:
            if md < r:
                used += md
            else:
                used += r
                
        if used <= m:
            mn = md + 1
            ans = md
        else:
            mx = md - 1
    max_req = max(req)
    print(ans if ans < max_req else max_req)
    
if __name__ == '__main__':
    solution()
