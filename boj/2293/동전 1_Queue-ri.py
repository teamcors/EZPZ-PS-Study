import sys
input = sys.stdin.readline
    
def solution():
    n, k = map(int, input().split())
    coins = []
    for _ in range(n):
        coins.append(int(input()))
    coins.sort()
    
    memo = [0] * (k+1)
    memo[0] = 1
    for c in coins:
        for i in range(c, k+1):
            memo[i] += memo[i - c]
    
    print(memo[k])

if __name__ == '__main__':
    solution()