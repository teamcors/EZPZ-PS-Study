import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    data = sorted(set(map(int, input().split())))
    ans = combinations_with_replacement(data, m)
    for e in ans:
        print(*e)


if __name__ == '__main__':
    solution()