import sys
input = sys.stdin.readline
    
def solution():
    n = int(input())
    series = [0] * 10000
    for i in range(n):
        series[i] = int(input())
    memo = [0] * 10000
    
    memo[0] = series[0]
    memo[1] = series[0] + series[1]
    memo[2] = max(series[2]+series[0], series[2]+series[1], memo[1])
    
    for i in range(3, n):
        memo[i] = max(series[i]+memo[i-2], series[i]+series[i-1]+memo[i-3], memo[i-1])
    
    print(max(memo))

if __name__ == '__main__':
    solution()