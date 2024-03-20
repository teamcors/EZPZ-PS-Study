import sys
from math import inf
from itertools import combinations
input = sys.stdin.readline

ans, N = 0, 0
egg = []

def dfs(start):
    global ans
    
    if start == N:
        total = 0
        for i in range(N):
            if egg[i][0] <= 0:
                total += 1

        ans = max(ans,total)
        return

    if egg[start][0] <= 0:
        dfs(start+1)
        return

    check = True
    for i in range(N):
        if i == start:
            continue
        if egg[i][0] > 0:
            check = False
            break

    if check: #다 깨져있는 경우
        ans = max(ans, N-1) #자기빼고 전부다니깐 N-1
        return

    for i in range(N):
        if i == start or egg[i][0] <= 0:
            continue
        egg[start][0] -= egg[i][1]
        egg[i][0] -= egg[start][1]
        dfs(start+1)
        egg[start][0] += egg[i][1]
        egg[i][0] += egg[start][1]


def solution():
    global N, egg
    N = int(input())
    egg = [list(map(int,input().split())) for _ in range(N)]
    dfs(0)
    
    print(ans)

if __name__ == '__main__':
    solution()