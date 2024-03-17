import sys
from itertools import combinations
input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    series = sorted(map(int, input().split()))
    comb = sorted(set(combinations(series, m)))
    for x in comb:
        print(*x)
    
if __name__ == '__main__':
    solution()
