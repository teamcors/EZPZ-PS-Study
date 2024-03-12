import sys

input = sys.stdin.readline

n = int(input())
values = list(map(int, input().split()))
values.sort()

left, right = 0, n - 1
answer_v = abs(values[left] + values[right])
answer = [values[0], values[-1]]

while left < right:
    s = values[left] + values[right]

    if abs(s) < answer_v:
        answer_v = abs(s)
        answer = [values[left], values[right]]
        if answer == 0:
            break
    if s < 0:
        left += 1
    else:
        right -= 1

print(*answer)
