import sys

input = sys.stdin.readline

n, s = map(int, input().split())
numbers = list(map(int, input().split()))
answer = 0


def sum_(i, sum):
    global answer

    if i >= n:
        return

    sum += numbers[i]

    if sum == s:
        answer += 1

    sum_(i + 1, sum)
    sum_(i + 1, sum - numbers[i])


sum_(0, 0)
print(answer)
