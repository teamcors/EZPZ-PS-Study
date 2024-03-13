import sys
from sys import stdin

k, n = map(int, input().split())
lis = []
for _ in range(k):
    lis.append(int(input()))

start = 1
end = max(lis)

while (start <= end):
    mid = (start + end) // 2
    cnt = 0
    for i in range(k):
        cnt += lis[i] // mid
    if cnt >= n:
        start = mid + 1
    else:
        end = mid -1
print(end)
    

