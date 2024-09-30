import sys
from itertools import combinations
input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    data = sorted(data)
    
    ans = sorted(set([x for x in combinations(data, m)]))
    for e in ans:
        print(*e)

if __name__ == '__main__':
    solution()
