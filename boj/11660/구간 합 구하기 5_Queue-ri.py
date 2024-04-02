import sys
input = sys.stdin.readline
    
def solution():
    n, m = map(int, input().split())
    table = []
    for _ in range(n):
        table.append(list(map(int,input().split())))
    
    memo = [[0 for _ in range(n+1)] for __ in range(n+1)]
    for y in range(1, n+1):
        for x in range(1, n+1):
            memo[y][x] = table[y-1][x-1] + memo[y-1][x] + memo[y][x-1] - memo[y-1][x-1]
    
    for _ in range(m):
        x1, y1, x2, y2 = map(int, input().split())
        ans = memo[x2][y2] - memo[x2][y1-1] - memo[x1-1][y2] + memo[x1-1][y1-1]
        print(ans)

if __name__ == '__main__':
    solution()