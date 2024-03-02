import sys
from collections import defaultdict
input = sys.stdin.readline

def dfs(world, dd, prev_str, n, m, y, x, length):
    dy = [-1, -1, -1, 0, 0, 1, 1, 1]
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]
    
    if length > 5:
        return
    
    cur_str = prev_str + world[y][x]
    dd[cur_str] += 1
    
    for i in range(8):
        ny = (y + dy[i]) % n
        nx = (x + dx[i]) % m
        dfs(world, dd, cur_str, n, m, ny, nx, length+1)
    
def solution():
    n, m, k = map(int, input().split())
    world = [0] * n
    for y in range(n):
        world[y] = list(input().rstrip())
        
    # 가능한 모든 문자열 계산
    dd = defaultdict(int)
    for y in range(n):
        for x in range(m):
            dfs(world, dd, '', n, m, y, x, 1)
    
    # 각 문자열마다 경우의 수 출력
    for i in range(k):
        s = input().rstrip()
        print(dd[s])


if __name__ == '__main__':
    solution()
