import sys
input = sys.stdin.readline

def solution():
    k, n = map(int, input().split())
    lans = []
    minl, maxl = 1, -1
    for _ in range(k):
        l = int(input())
        maxl = max(maxl, l)
        lans.append(l)
        
    ans = 0
    while minl <= maxl:
        midl = int((minl+maxl)/2)
        cnt = 0
        for x in lans:
            cnt += int(x/midl)
            
        if n <= cnt:
            minl = midl + 1
            ans = midl
        else:
            maxl = midl - 1
            
    print(ans)
    
if __name__ == '__main__':
    solution()
