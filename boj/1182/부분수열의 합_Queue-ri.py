import sys
from itertools import combinations
input = sys.stdin.readline

def solution():
    n, s = map(int, input().split())
    seq = list(map(int, input().split()))
    
    ans = 0
    for size in range(1, len(seq)+1):
        sums = [sum(x) for x in combinations(seq, size)]
        for k in sums:
            if k == s:
                ans += 1
                
    print(ans)
        
    
if __name__ == '__main__':
    solution()
