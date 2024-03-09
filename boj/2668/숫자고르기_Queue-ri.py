import sys
input = sys.stdin.readline

adj = []
visited = []
ans = []

def dfs(k, start):
    global visited, ans
    
    if visited[k]:
        return k == start # valid cycle?
    
    visited[k] = True
    res = dfs(adj[k], start)
    visited[k] = res # keep visited if valid cycle else recover
    if res:
        ans.append(k)
    return res

def solution():
    global adj, visited
    n = int(input())
    adj = [0 for _ in range(n+1)]
    visited = [False for _ in range(n+1)]
    for k in range(1, n+1):
        adj[k] = int(input())
    
    for k in range(1, n+1):
        if not visited[k]:
            dfs(k, k)
        
    print(len(ans))
    print('\n'.join([str(x) for x in sorted(ans)]))


if __name__ == '__main__':
    solution()
