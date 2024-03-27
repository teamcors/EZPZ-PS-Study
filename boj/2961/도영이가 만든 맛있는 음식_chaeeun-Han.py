# 17min 14sec
import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
minCook = 1000000000

for i in range(1, n+1):
    for combi in (combinations(data, i)):
        sour, bitter = 1, 0
        for s, b in combi:
            sour *= s
            bitter += b
        minCook = min(abs(sour-bitter), minCook)
print(minCook)
