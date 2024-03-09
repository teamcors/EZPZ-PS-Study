import sys
from collections import deque
input = sys.stdin.readline

red_pos = []
box = []
m, n, h = 0, 0, 0

def bfs():
    global box
    q = deque()
    for x in red_pos:
        q.append(x)
    
    di = [-1, 1, 0, 0, 0, 0]
    dj = [0, 0, -1, 1, 0, 0]
    dk = [0, 0, 0, 0, -1, 1]
    
    lapsed, reds = 0, 0
    while q:
        i, j, k, cnt = q.popleft()
        for d in range(6):
            ni = i + di[d]
            nj = j + dj[d]
            nk = k + dk[d]
            nday = cnt + 1
            
            if (-1<ni<h) and (-1<nj<n) and (-1<nk<m):
                if box[ni][nj][nk] == 0:
                    q.append((ni, nj, nk, nday))
                    box[ni][nj][nk] = nday # visited
                    lapsed = max(lapsed, nday)
                    reds += 1
    
    return lapsed, reds
    

def solution():
    global box, m, n, h
    m, n, h = map(int, input().split())
    box = [[[] for __ in range(n)] for ___ in range(h)]
    greens = 0
    for z in range(h):
        for y in range(n):
            box[z][y].extend(list(map(int, input().split())))
            for x in range(m):
                if not box[z][y][x]:
                    greens += 1
    
    global red_pos
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if box[i][j][k] == 1:
                    red_pos.append((i, j, k, 1))
                    
    if greens == 0: # edge case
        print(0)
        return
    
    lapsed, reds = bfs()
    
    print(-1 if reds != greens else lapsed-1)

if __name__ == '__main__':
    solution()
