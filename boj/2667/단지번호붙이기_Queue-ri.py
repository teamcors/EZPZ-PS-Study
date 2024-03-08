import sys
from collections import deque
input = sys.stdin.readline

table = []

def dfs(y, x, n):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    cnt = 1
    
    table[y][x] = 0
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if -1 < ny and ny < n and -1 < nx and nx < n and table[ny][nx]:
            cnt += dfs(ny, nx, n)
        
    return cnt
    
    
def solution():
    global table
    n = int(input())
    for i in range(n):
        table.append([int(x) for x in input().rstrip()])
        
    ans = []
    for y in range(n):
        for x in range(n):
            if table[y][x]:
                ans.append(dfs(y, x, n))
                    
    ans = sorted(ans)
    print(len(ans))
    for k in ans:
        print(k)
    
    
if __name__ == '__main__':
    solution()
