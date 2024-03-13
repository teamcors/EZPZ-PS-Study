import sys
from sys import stdin

n, m = map(int, input().split())
level = [sys.stdin.readline().split() for _ in range(n)]
level.sort(key=lambda x:int(x[1]))
score = [int(sys.stdin.readline().strip()) for _ in range(m)]
for score in score:
    right = len(level)
    left = 0
    result = 0
    while left <= right :
        mid = (left+right) // 2
        if int(level[mid][1]) >= score:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    print(level[result][0])


