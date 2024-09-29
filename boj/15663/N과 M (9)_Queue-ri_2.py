import sys
from itertools import permutations
input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    data = map(int, input().split())
    data = sorted(data)
    comb = set(x for x in permutations(data, m))
    comb = sorted(comb)
    for x in comb:
        for e in x:
            print(e, end=' ')
        print()

if __name__ == '__main__':
    solution()