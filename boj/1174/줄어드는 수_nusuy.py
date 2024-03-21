import sys
input = sys.stdin.readline

arr = []
result = []

def dfs():
    if len(arr) > 0:
        result.append(int("".join(map(str, arr))))

    for i in range(10):
        if len(arr) == 0 or arr[-1] > i:
            arr.append(i)
            dfs()
            arr.pop()

n = int(input())

try:
    dfs()
    result.sort()
    print(result[n - 1])
except:
    print(-1)
