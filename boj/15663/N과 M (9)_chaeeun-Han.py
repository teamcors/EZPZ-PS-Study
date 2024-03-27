# 24min 21sec
import sys
from itertools import permutations

input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))
result = set()

for combi in permutations(data, m):
    result.add(tuple(combi))

for answer in sorted(result):
    print(*answer)
