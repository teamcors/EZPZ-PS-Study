import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    memo = [0] * (n+1)
    for i in range(1, n+1):
        t, p = map(int, input().split())
        memo[i] = max(memo[i-1], memo[i])
        if i+t <= n+1:
            memo[i+t-1] = max(memo[i-1]+p, memo[i+t-1])
    
    print(memo[-1])

if __name__ == '__main__':
    solution()