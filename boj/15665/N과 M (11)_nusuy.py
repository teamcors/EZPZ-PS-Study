import sys

input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()
arr = []


def check(n, m, depth):
    if depth == m:
        print(" ".join(map(str, arr)))
        return

    prev = -1
    for number in numbers:
        if number != prev:
            arr.append(number)
            check(n, m, depth + 1)
            arr.pop()
            prev = number


check(n, m, 0)
