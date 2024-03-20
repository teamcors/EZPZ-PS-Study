import sys
from itertools import combinations
input = sys.stdin.readline

def solution():
    n = int(input())
    res = []
    for i in range(1, 11):
        for c in combinations(range(0, 10), i):
            comb = sorted(list(c), reverse=True)
            res.append(int("".join(map(str, comb))))
        
        if n < len(res):
            break
    res.sort()
    
    try:
        print(res[n - 1])
    except:
        print(-1)
    
    
if __name__ == '__main__':
    solution()