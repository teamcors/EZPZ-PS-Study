import sys

input = sys.stdin.readline

n, m = map(int, input().split())
times = []
for i in range(n):
    times.append(int(input()))


def solution(n, m, times):
    answer = 0

    left, right = 1, max(times) * m
    while left <= right:
        mid = (left + right) // 2
        people = 0

        for time in times:
            people += mid // time

            if people >= m:
                break
        if people >= m:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer


print(solution(n, m, times))
