import sys
input = sys.stdin.readline

def solution():
    n, k = map(int, input().split())
    items = []
    for _ in range(n):
        w, v = map(int, input().split())
        items.append((w, v))
    memo = [0 for _ in range(k+1)]
    
    for item in items:
        w, v = item
        for i in range(k, w-1, -1):
            memo[i] = max(memo[i], memo[i-w] + v)
    
    print(memo[-1])

if __name__ == '__main__':
    solution()