import sys
from collections import deque
input = sys.stdin.readline

def solution():
    n, t = map(int, input().split())
    
    points = set()
    for i in range(n):
        x, y = map(int, input().split())
        points.add((x, y))
        
    # bfs
    q = deque()
    q.append([0, 0, 0])
    ans = -1
    while q:
        x, y, cnt = q.popleft()
        
        if y == t:
            ans = cnt
            break
        
        for i in range(-2, 3):
            for j in range(-2, 3):
                nx = x + i
                ny = y + j
                if (nx, ny) in points:
                    q.append([nx, ny, cnt+1])
                    points.remove((nx, ny))

    print(ans)


if __name__ == '__main__':
    solution()
