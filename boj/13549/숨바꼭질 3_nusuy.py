import sys
from collections import deque
input = sys.stdin.readline

def solution(N, K):
    visited = [0 for _ in range(100001)]
    q = deque([N])
    while q:
        x = q.popleft()
        if x == K:
            return visited[x]

        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx < 100001 and visited[nx] == 0:
                if nx == x * 2 and nx != 0:
                    visited[nx] = visited[x]
                    q.appendleft(nx)
                else:
                    visited[nx] = visited[x] + 1
                    q.append(nx)

N, K = map(int, input().split())
print(solution(N, K))
