from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    # padding
    visited = [[0 for _ in range(m+2)]]
    for i in range(n):
        visited.append([0] + maps[i] + [0])
    visited.append([0 for _ in range(m+2)])
    
    q = deque()
    q.append((1,1,1))
    visited[1][1] = 0
    
    while q:
        y, x, depth = q.popleft()
        if y == n and x == m:
            return depth
        if visited[y-1][x]:
            q.append((y-1, x, depth+1))
            visited[y-1][x] = 0
        if visited[y+1][x]:
            q.append((y+1, x, depth+1))
            visited[y+1][x] = 0
        if visited[y][x-1]:
            q.append((y, x-1, depth+1))
            visited[y][x-1] = 0
        if visited[y][x+1]:
            q.append((y, x+1, depth+1))
            visited[y][x+1] = 0
        
    return -1
