import sys
input = sys.stdin.readline

def solution(n, numbers):
    d = [0] * n
    d[0] = numbers[0]
    for i in range(1, n):
        d[i] = numbers[i]
        for j in range(i + 1):
            if numbers[i] > numbers[i - j]:
                d[i] = max(d[i], d[i - j] + numbers[i])
    return max(d)

n = int(input())
numbers = list(map(int, input().split()))

print(solution(n, numbers))
