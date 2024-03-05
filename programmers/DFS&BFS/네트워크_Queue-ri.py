visited = []
adj = []

def dfs(v, n):
    global visited, adj
    visited[v] = True
    for i in range(n):
        if adj[v][i] and not visited[i]:
            dfs(i, n)
            
    return

def solution(n, computers):
    global visited, adj
    visited = [False for _ in range(n)]
    adj = computers
    ans = 0
    for i in range(n):
        if not visited[i]:
            ans += 1
            dfs(i, n)
    
    return ans