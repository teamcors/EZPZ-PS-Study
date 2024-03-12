import sys

input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

left, right = 0, max(trees)
answer = 0
while left <= right:
    mid = (left + right) // 2
    a = 0
    for tree in trees:
        dff = tree - mid
        if dff > 0:
            a += dff
        if a >= m:
            break
    if a >= m:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1
print(answer)
