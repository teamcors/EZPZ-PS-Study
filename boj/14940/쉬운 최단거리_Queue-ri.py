import sys
from collections import deque
input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    table = []
    ans = [[-1 for _ in range(m)] for __ in range(n)]
    for i in range(n):
        table.append([int(x) for x in input().rstrip().split(' ')])
    
    sy, sx = -1, -1
    for i in range(n):
        for j in range(m):
            if table[i][j] == 2:
                sy = i
                sx = j
            if not table[i][j]:
                ans[i][j] = 0
                
    q = deque()
    q.append((sy, sx, 0))
    table[sy][sx] = 0 # visited
    
    while q:
        y, x, cnt = q.popleft()
        ans[y][x] = cnt
        
        dy = [-1, 1, 0, 0]
        dx = [0, 0, -1, 1]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if -1 < ny and ny < n and -1 < nx and nx < m and table[ny][nx]:
                q.append((ny, nx, cnt+1))
                table[ny][nx] = 0
                
    for x in ans:
        print(' '.join([str(e) for e in x]))
    
if __name__ == '__main__':
    solution()
