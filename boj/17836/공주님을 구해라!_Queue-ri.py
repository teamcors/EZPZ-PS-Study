import sys
from collections import deque
input = sys.stdin.readline

n, m = 0, 0
world = []
gpos = ()

def bfs():
    global world
    q = deque()
    q.append((1, 1, 0))
    world[1][1] = 1
    
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    
    s2g = -1
    s2p = -1
    while q:
        y, x, t = q.popleft()
        if y == gpos[0] and x == gpos[1]:
            s2g = t
        if y == n and x == m:
            s2p = t
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            nt = t + 1
            if (0<ny<=n) and (0<nx<=m) and world[ny][nx] == 0:
                q.append((ny, nx, nt))
                world[ny][nx] = 1
                
    return s2g, s2p

def solution():
    global n, m, world, visited, gpos
    n, m, t = map(int, input().split())
    gpos = (-1, -1)
    world.append([1 for _ in range(m+1)])
    
    for i in range(1, n+1):
        world.append([1] + list(map(int, input().split())))
        for j in range(m+1):
            if world[i][j] == 2:
                gpos = (i, j)
                world[i][j] = 0
                
    s2g, s2p = bfs()
    
    best = t+1
    g2p = (n-gpos[0]) + (m-gpos[1])
    if s2p != -1 and s2g != -1:
        best = min(s2p, s2g+g2p)
    elif s2p != -1 and s2g == -1:
        best = s2p
    elif s2p == -1 and s2g != -1:
        best = s2g + g2p
    
    return 'Fail' if t < best else best

if __name__ == '__main__':
    print(solution())
