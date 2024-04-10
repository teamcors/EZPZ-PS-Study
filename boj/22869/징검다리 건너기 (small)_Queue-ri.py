import sys
input = sys.stdin.readline
    
def solution():
    n, k = map(int, input().split())
    rock = list(map(int, input().split()))
    memo = [0] * n
    memo[0] = 1
    
    for i in range(n-1):
        for j in range(i+1, n):
            if memo[i] and (j - i) * (1 + abs(rock[j] - rock[i])) <= k:
            	memo[j] = 1
    
    print("YES" if memo[n-1] else "NO")

if __name__ == '__main__':
    solution()