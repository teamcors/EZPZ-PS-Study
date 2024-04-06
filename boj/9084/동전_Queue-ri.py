import sys
input = sys.stdin.readline
    
def solution():
    tc = int(input())
    for _ in range(tc):
        n = int(input())
        coins = list(map(int, input().split()))
        m = int(input())
        memo = [0] * (m+1)
        memo[0] = 1
    
        for c in coins:
            for i in range(m+1):
                if i >= c:
                    memo[i] += memo[i-c]
    
        print(memo[m])

if __name__ == '__main__':
    solution()