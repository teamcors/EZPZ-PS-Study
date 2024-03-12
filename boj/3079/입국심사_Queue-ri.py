import sys
input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    times = []
    for _ in range(n):
        times.append(int(input()))
    
    ans = 0
    minT, maxT = 1, int(10e9)*m
    while minT <= maxT:
        midT = (minT + maxT) // 2
        total = 0
        for i in range(n):
            total += (midT // times[i])
            
        if m <= total:
            ans = midT
            maxT = midT - 1
        else:
            minT = midT + 1
            
    print(ans)
    
    
if __name__ == '__main__':
    solution()
