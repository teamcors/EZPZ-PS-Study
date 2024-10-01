import sys
from itertools import combinations
input = sys.stdin.readline

def solution():
    n = int(input())
    lst = []
    
    for size in range(1, 11):
        for x in combinations(range(0, 10), size):
            pair = sorted(x, reverse=True)
            lst.append(int("".join(map(str, pair))))
        if n <= len(lst):
            break
        
    lst.sort()
    
    if n <= len(lst):
        print(lst[n-1])
    else:
        print(-1)

if __name__ == "__main__":
    solution()