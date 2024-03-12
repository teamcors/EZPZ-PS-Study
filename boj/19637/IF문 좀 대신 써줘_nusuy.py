import sys

input = sys.stdin.readline

n, m = map(int, input().split())
titles = []
for i in range(n):
    titles.append(input().split())


def find_title(cp):
    left, right = 0, len(titles) - 1
    while True:
        mid = (left + right) // 2
        if left >= right:
            print(titles[mid][0])
            break
        if int(titles[mid][1]) >= cp:
            right = mid
        else:
            left = mid + 1


for i in range(m):
    find_title(int(input()))
