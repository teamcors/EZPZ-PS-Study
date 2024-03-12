import sys

input = sys.stdin.readline

n = int(input())
reqs = list(map(int, input().split()))
m = int(input())
mx = max(reqs)
left, right = 0, mx
answer = 0
while left <= right:
    mid = (left + right) // 2
    M = m
    limited = 0
    for req in reqs:
        budget = req
        if req > mid:
            budget = mid
            limited += 1
        M -= budget
    if M < 0:
        right = mid - 1
    elif M == 0:
        answer = mid
        break
    else:
        if (limited != 0 and M // limited == 0) or mid == mx:
            answer = mid
            break
        left = mid + 1
print(answer)
