import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    series = sorted(set(map(int, input().split())))
    cwr = combinations_with_replacement(series, m)
    for x in cwr:
        print(*x)
    
    
if __name__ == '__main__':
    solution()
