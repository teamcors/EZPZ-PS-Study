import sys
from itertools import product
input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    ans = sorted(set(product(data, repeat=m)))
    for e in ans:
        print(*e)

if __name__ == '__main__':
    solution()