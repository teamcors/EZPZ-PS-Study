import sys
input = sys.stdin.readline

def solution(n, numbers):
    # d[n]: n 번째 원소까지 고려한 경우의 최대 연속합
    d = [0] * n
    d[0] = numbers[0]

    for i in range(1, n):
        d[i] = max(numbers[i], d[i - 1] + numbers[i])

    return max(d)

n = int(input())
numbers = list(map(int, input().split()))

print(solution(n, numbers))
