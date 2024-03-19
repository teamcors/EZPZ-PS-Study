from math import inf
import sys

input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))  # + - * /
mn, mx = inf, -inf


def operate(idx, value):
    global mn, mx
    if idx == n:
        mn = min(mn, value)
        mx = max(mx, value)
        return

    for i in range(4):
        if operators[i] <= 0:
            continue
        operators[i] -= 1
        if i == 0:
            operate(idx + 1, value + numbers[idx])
        elif i == 1:
            operate(idx + 1, value - numbers[idx])
        elif i == 2:
            operate(idx + 1, value * numbers[idx])
        else:
            operate(idx + 1, int(value / numbers[idx]))
        operators[i] += 1


operate(1, numbers[0])
print(mx, mn, sep="\n")
