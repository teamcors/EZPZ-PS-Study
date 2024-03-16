import sys

input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()


def check(idx, arr):
    if len(arr) >= m:
        print(" ".join(map(str, arr)))
        return

    prev = -1
    for i in range(idx, n):
        if numbers[i] != prev:
            arr.append(numbers[i])
            check(i, arr)
            arr.pop()
            prev = numbers[i]


check(0, [])
