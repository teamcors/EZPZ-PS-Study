# 1min 47sec
import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
result = set()

for combi in combinations_with_replacement(data, m):
    result.add(tuple(combi))

for answer in sorted(result):
    print(*answer)
