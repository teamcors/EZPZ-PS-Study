import sys
from collections import deque
input = sys.stdin.readline

m, n = 0, 0
box = []
red_pos = []

def bfs():
    q = deque()
    for x in red_pos:
        q.append(x)
        
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    
    reds, lapsed = 0, 0
    while q:
        i, j, cnt = q.popleft()
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            nday = cnt + 1
            if (-1<ni<n) and (-1<nj<m) and box[ni][nj] == 0:
                q.append((ni, nj, nday))
                box[ni][nj] = nday
                lapsed = max(lapsed, nday)
                reds += 1
    return reds, lapsed

def solution():
    global m, n, box, red_pos
    m, n = map(int, input().split())
    greens = 0
    for i in range(n):
        box.append(list(map(int, input().split())))
        for j in range(m):
            if box[i][j] == 0:
                greens += 1
            if box[i][j] == 1:
                red_pos.append((i, j, 0))
    
    reds, lapsed = bfs()
    if greens == 0:
        print(0)
        return
    print(lapsed if reds == greens else -1)

if __name__ == '__main__':
    solution()
