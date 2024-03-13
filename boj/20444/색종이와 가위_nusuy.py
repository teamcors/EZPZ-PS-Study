import sys

input = sys.stdin.readline

n, k = map(int, input().split())


def solution(n, k):
    left, right = 0, n // 2
    while left <= right:
        mid = (left + right) // 2
        count = (mid + 1) * (n - mid + 1)
        if count == k:
            return "YES"
        elif count > k:
            right = mid - 1
        else:
            left = mid + 1
    return "NO"


print(solution(n, k))
