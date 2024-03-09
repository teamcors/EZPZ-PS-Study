import sys
from collections import deque
from copy import deepcopy
from itertools import combinations
input = sys.stdin.readline

n, m = 0, 0
table, vpos = [], []
ans = -1

def contaminate(): # bfs
    global ans
    table_cp = deepcopy(table)
    q = deque()
    for x in vpos:
        q.append(x)
    
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if -1 < ny and ny < n and -1 < nx and nx < m and table_cp[ny][nx] == 0:
                q.append((ny, nx))
                table_cp[ny][nx] = 2
    
    cnt = 0
    for i in range(n):
        for j in range(m):
            if table_cp[i][j] == 0:
                cnt += 1
    
    #print(table_cp, cnt)
    ans = max(ans, cnt)

def solution():
    global n, m, table, vpos
    n, m = map(int, input().split())
    table = []
    zpos = []
    for i in range(n):
        table.append(list(map(int, input().split())))
        for j in range(m):
            if table[i][j] == 2:
                vpos.append((i, j))
            elif table[i][j] == 0:
                zpos.append((i, j))
    
    walls = list(combinations(zpos, 3))
    for w in walls:
        w1, w2, w3 = w
        table[w1[0]][w1[1]] = 1
        table[w2[0]][w2[1]] = 1
        table[w3[0]][w3[1]] = 1
        contaminate()
        table[w1[0]][w1[1]] = 0
        table[w2[0]][w2[1]] = 0
        table[w3[0]][w3[1]] = 0
        
    print(ans)
                

if __name__ == '__main__':
    solution()
