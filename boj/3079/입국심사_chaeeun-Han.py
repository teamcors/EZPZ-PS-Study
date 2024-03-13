import sys
input = sys.stdin.readline

def binary_search(n, m, times):
    left, right = 1, min(times) * m

    while left <= right:
        mid = (left + right) // 2
        total_people = sum(mid // time for time in times)

        if total_people >= m:
            right = mid - 1
        else:
            left = mid + 1

    return left

n, m = map(int, input().split())
times = [int(input()) for _ in range(n)]
print(binary_search(n, m, times))
