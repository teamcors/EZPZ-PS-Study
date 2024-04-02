import sys
input = sys.stdin.readline
    
def solution():
    n, m = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(n)]
    
    memo = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            memo[i][j] = area[i-1][j-1] + memo[i-1][j] + memo[i][j-1] - memo[i-1][j-1]
    
    k = int(input())
    for _ in range(k):
        x1, y1, x2, y2 = map(int, input().split())
        print(memo[x2][y2] - memo[x1-1][y2] - memo[x2][y1-1] + memo[x1-1][y1-1])

if __name__ == '__main__':
    solution()