import sys
input = sys.stdin.readline

def solution(n, numbers):
    d = [1] * n
    for i in range(1, n):
        for j in range(i + 1):
            if numbers[i] > numbers[i - j]:
                d[i] = max(d[i], d[i - j] + 1)
    return max(d)

n = int(input())
numbers = list(map(int, input().split()))

print(solution(n, numbers))
