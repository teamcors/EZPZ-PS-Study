# 4min 19sec
import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
result = set()

for combi in combinations(data, m):
    result.add(tuple(combi))

for answer in sorted(result):
    print(*answer)
