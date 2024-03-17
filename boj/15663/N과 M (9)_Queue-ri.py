import sys
from itertools import permutations
input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    series = map(int, input().split())
    perm = permutations(series, m)
    perm = sorted(set(perm))
    for x in perm:
        print(*x)
    
    
if __name__ == '__main__':
    solution()
