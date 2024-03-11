import sys

input = sys.stdin.readline

n, m = map(int, input().split())
points = list(map(int, input().split()))
lines = []
for i in range(m):
    a, b = map(int, input().split())
    lines.append((a, b))

points.sort()


def find_mn(line):
    a, b = line
    left, right = 0, len(points) - 1
    answer = -1
    while left <= right:
        mid = (left + right) // 2
        if points[mid] >= a:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer


def find_mx(line):
    a, b = line
    left, right = 0, len(points) - 1
    answer = -1
    while left <= right:
        mid = (left + right) // 2
        if points[mid] <= b:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    return answer


for line in lines:
    mn = find_mn(line)
    mx = find_mx(line)
    if mn == -1 or mx == -1:
        print(0)
    else:
        print(mx - mn + 1)
