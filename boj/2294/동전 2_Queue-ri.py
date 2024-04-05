import sys
input = sys.stdin.readline
    
def solution():
    n, k = map(int, input().split())
    coins = []
    for _ in range(n):
        coins.append(int(input()))
        
    memo = [10001] * (k+1)
    memo[0] = 0
    for c in coins:
        for i in range(c, k+1):
            if memo[i] > 0:
                memo[i] = min(memo[i], memo[i-c]+1)
    
    print(-1 if memo[k] == 10001 else memo[k])

if __name__ == '__main__':
    solution()