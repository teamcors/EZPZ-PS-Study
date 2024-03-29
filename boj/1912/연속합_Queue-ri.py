import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    series = list(map(int, input().split()))
    
    memo = [0] * n
    memo[0] = series[0]
    for i in range(1, n):
        memo[i] = max(series[i], memo[i-1]+series[i])
    print(max(memo))

if __name__ == '__main__':
    solution()