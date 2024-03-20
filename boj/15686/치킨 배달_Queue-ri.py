import sys
from math import inf
from itertools import combinations
input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    city = list(list(map(int, input().split())) for _ in range(n))
    house, chick = [], []
    
    for i in range(n):
        for j in range(n):
            if city[i][j] == 1:
                house.append([i, j])
            elif city[i][j] == 2:
                chick.append([i, j])
    
    res = inf
    for comb in combinations(chick, m):
        tmp = 0
        for h in house: 
            chi_len = inf
            for j in range(m):
                chi_len = min(chi_len, abs(h[0] - comb[j][0]) + abs(h[1] - comb[j][1]))
            tmp += chi_len
        res = min(res, tmp)
    
    print(res)

if __name__ == '__main__':
    solution()