import sys
from math import inf
from itertools import combinations
input = sys.stdin.readline

def solution():
    n = int(input())
    data = []
    for i in range(n):
        data.append(list(map(int, input().split())))
    
    ans = inf
    for size in range(1, len(data)+1):
        res = [x for x in combinations(data, size)]
        
        for x in res:
            sour = 1
            bitter = 0
            for idx in range(len(x)):
                sour *= x[idx][0]
                bitter += x[idx][1]
            
            diff = abs(sour - bitter)
            if diff < ans:
                ans = diff
    print(ans)
    
    
if __name__ == '__main__':
    solution()