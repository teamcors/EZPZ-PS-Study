import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    series = list(map(int, input().split()))
    
    memo = [1] * n
    for i in range(1, n):
        for j in range(i):
            if series[i] > series[j]:
                memo[i] = max(memo[i], memo[j]+1)
 
    print(max(memo))

if __name__ == '__main__':
    solution()