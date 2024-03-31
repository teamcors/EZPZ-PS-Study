import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    series = list(map(int, input().split()))
    
    memo = [1] * n
    memo[0] = series[0]
    for i in range(1, n):
        for j in range(i):
            if series[j] < series[i]:
                memo[i] = max(memo[i], memo[j] + series[i])
            else:
                memo[i] = max(memo[i], series[i])
    
    print(max(memo))

if __name__ == '__main__':
    solution()