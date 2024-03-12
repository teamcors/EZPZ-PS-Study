import sys

input = sys.stdin.readline

k, n = map(int, input().split())
length = [0 for _ in range(k)]
for i in range(k):
    length[i] = int(input())

left, right = 1, max(length)
answer = 0
while left <= right:
    mid = (left + right) // 2
    lan = 0
    for l in length:
        lan += l // mid
    if lan >= n:
        left = mid + 1
        answer = mid
    elif lan < n:
        right = mid - 1

print(answer)
