import sys

input = sys.stdin.readline


def solution():
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    numbers.sort()

    answers = []

    def check(n, m, numbers, idx, arr):
        if len(arr) == m:
            if arr not in answers:
                answers.append(arr[:])
            return
        if idx >= n:
            return
        for i in range(idx, n):
            arr.append(numbers[i])
            check(n, m, numbers, i + 1, arr)
            arr.pop()

    check(n, m, numbers, 0, [])
    for a in answers:
        print(*a)


if __name__ == "__main__":
    solution()
