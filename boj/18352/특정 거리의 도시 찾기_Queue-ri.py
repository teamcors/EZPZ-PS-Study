import sys
from collections import deque
input = sys.stdin.readline

def solution():
    n, m, k, x = map(int, input().split())
    adj = [[] for _ in range(n+1)]
    ans = [-1 for _ in range(n+1)]
    
    visited = [False for _ in range(n+1)]
    for i in range(m):
        a, b = map(int, input().split())
        adj[a].append(b)
        
    q = deque()
    q.append((x, 0))
    visited[x] = True
    
    while q:
        v, length = q.popleft()
        ans[v] = length
        for nxt_v in adj[v]:
            if not visited[nxt_v]:
                q.append((nxt_v, length+1))
                visited[nxt_v] = True
    
    none = True
    for i, length in enumerate(ans):
        if length == k:
            none = False
            print(i)

    if none:
        print(-1)

if __name__ == '__main__':
    solution()
