import sys
input = sys.stdin.readline
    
def solution():
    n = int(input())
    num = list(map(int, input().split()))
    memo = [[0]*21 for i in range(n-1)]
    memo[0][num[0]] = 1
    
    for i in range(1, n-1):
        for j in range(21):
            if j - num[i] >= 0: memo[i][j-num[i]] += memo[i-1][j]
            if j + num[i] <= 20: memo[i][j+num[i]] += memo[i-1][j]
    
    print(memo[-1][num[-1]])

if __name__ == '__main__':
    solution()