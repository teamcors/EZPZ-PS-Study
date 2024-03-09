import sys
input = sys.stdin.readline

adj = []
visited = []

def dfs(cur, nxt, depth):
    global visited
    
    if depth == 4:
        return True
    
    visited[cur] = True
    for nnxt in adj[nxt]:
        if not visited[nnxt]:
            if dfs(nxt, nnxt, depth+1):
                return True
    
    visited[cur] = False
    return False

def solution():
    global adj, visited
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    visited = [False for _ in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
    
    for i in range(n):
        for x in adj[i]:
            if dfs(i, x, 1):
                return 1
                
    return 0

if __name__ == '__main__':
    print(solution())
