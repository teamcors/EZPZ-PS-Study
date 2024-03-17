import sys
from itertools import product
input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    series = set(map(int, input().split()))
    pro = sorted(product(series, repeat=m))
    for x in pro:
        print(*x)
    
if __name__ == '__main__':
    solution()
