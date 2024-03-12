import sys
input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    trees = list(map(int, input().split()))
    
    ans = 0
    mn, mx = 0, int(1e9)
    while mn <= mx:
        h = (mn + mx) // 2
        got = 0
        for t in trees:
            if h < t:
                got += (t - h)
        
        if m <= got:
            mn = h + 1
            ans = h
        else:
            mx = h - 1
    print(ans)
    
if __name__ == '__main__':
    solution()
