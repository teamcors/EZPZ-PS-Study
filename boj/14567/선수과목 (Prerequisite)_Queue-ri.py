import sys
input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    res = [1] * (n+1)
    data = []
    for _ in range(m):
        a, b = map(int, input().split())
        data.append((a, b))
    data.sort()
    
    for a, b in data:
        if res[b] <= res[a]:
            res[b] = res[a] + 1
    
    print(*res[1:])

if __name__ == '__main__':
    solution()