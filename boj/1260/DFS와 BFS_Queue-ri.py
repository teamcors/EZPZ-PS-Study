import sys
from collections import deque, defaultdict
input = sys.stdin.readline

def dfs(visited, adj, v, n):
    path = []
    path.append(v)
    visited[v] = True
    
    for k in range(1, n+1):
        if adj[v][k] and not visited[k]:
            path.extend(dfs(visited, adj, k, n))
    
    return path


def bfs(visited, adj, v, n):
    path = []
    q = deque()
    q.append(v)
    visited[v] = True
    while q:
        k = q.popleft()
        path.append(k)
        for i in range(1, n+1):
            if adj[k][i] and not visited[i]:
                q.append(i)
                visited[i] = True
                
    return path


def solution():
    n, m, v = map(int, input().rsplit())
    adj = [[False for _ in range(n+1)] for __ in range(n+1)]
    
    for i in range(m):
        a, b = map(int, input().rsplit())
        adj[a][b] = adj[b][a] = True
    
    visited = [False] * (n+1)
    path = []
    path = dfs(visited, adj, v, n)
    print(' '.join(str(p) for p in path))
    
    visited = [False] * (n+1) 
    path = bfs(visited, adj, v, n)
    print(' '.join(str(p) for p in path))

if __name__ == '__main__':
    solution()