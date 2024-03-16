# 40min 08sec
import sys
input = sys.stdin.readline

n, m, l = map(int, input().split())
guns = sorted(list(map(int, input().split())))

def binary_search(x, y):
    start = 0
    end = n-1
    answer = 0

    while start <= end:
        mid = (start + end) // 2

        if abs(guns[mid]-x) + y <= l:
            answer += 1
            return answer
        elif guns[mid] < x:
            start = mid + 1
        else:
            end = mid - 1

    return answer

result = 0
for _ in range(m):
    x, y = map(int, input().split())
    result += binary_search(x, y)

print(result)
