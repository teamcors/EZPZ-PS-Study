import sys
from collections import deque
input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    miro = [[0 for _ in range(m+1)]]
    for i in range(n):
        x = list(int(x) for x in input().rstrip())
        miro.append([0] + x)
    
    q = deque()
    q.append((1, 1, 1))
    visited = [[False for _ in range(m+1)] for __ in range(n+1)]
    visited[1][1] = True
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while q:
        y, x, cnt = q.popleft()
        
        if y == n and x == m:
            return cnt
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 < ny and ny < n+1 and 0 < nx and nx < m+1 and miro[ny][nx] and not visited[ny][nx]:
                q.append((ny, nx, cnt+1))
                visited[ny][nx] = True
                
    return -1 # err
    

if __name__ == '__main__':
    print(solution())
