import sys

input = sys.stdin.readline


def solution():
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))

    visited = [False] * n
    answers = []

    def permuatation(n, m, numbers, arr):
        if len(arr) == m:
            answers.append(arr[:])
            return

        for i, v in enumerate(numbers):
            if not visited[i]:
                visited[i] = True
                arr.append(v)
                permuatation(n, m, numbers, arr)
                visited[i] = False
                arr.pop()

    permuatation(n, m, numbers, [])
    answers = sorted(list(set(map(tuple, answers))))
    for answer in answers:
        print(*answer)


if __name__ == "__main__":
    solution()
