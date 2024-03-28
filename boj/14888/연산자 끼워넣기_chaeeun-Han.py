# 44min 11sec
# a//b 과 int(a/b)의 차이
# a//b는 나눈 값을 내림처리를 진행하지만, int()는 소수점을 버리는 처리의 차이가 존재
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
arr = list(map(int, input().split()))
minimum, maximum = 1e9, -1e9


def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum
    if depth == n:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus:
        dfs(depth + 1, total + nums[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - nums[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * nums[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / nums[depth]),
            plus, minus, multiply, divide - 1)


dfs(1, nums[0], arr[0], arr[1], arr[2], arr[3])
print(maximum)
print(minimum)
