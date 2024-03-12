# 37min 14sec
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
datas = sorted(list(map(int, input().split())))

def binary_search(target, type):
    start = 0
    end = n-1

    while start <= end:
        mid = (start + end) // 2

        if datas[mid] == target:
            return mid
        elif datas[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    if type == 'l':
        return start
    else:
        return end

for _ in range(m):
    target1, target2 = map(int, input().split())
    l, r = binary_search(target1, 'l'), binary_search(target2, 'r')
    print(r-l+1)
