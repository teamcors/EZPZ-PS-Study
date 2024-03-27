# 5min 56sec
import sys
from itertools import product

input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
result = set()

for combi in product(data, repeat=m):
    result.add(tuple(combi))

for answer in sorted(result):
    print(*answer)
