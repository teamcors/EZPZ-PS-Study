import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = 0
ans = []
def dfs(root, adj, visited):
    global ans, n
    visited[root] = True
    for i in adj[root]:
        if not visited[i]:
            dfs(i, adj, visited)
            ans[i] = root
            
    return

def solution():
    global ans, n
    n = int(input())
    ans = [0] * (n+1)
    # matrix는 메모리 터짐 유의. list로 저장해야 함
    adj = [[] for _ in range(n+1)]
    
    for i in range(n-1):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
    
    visited = [False] * (n+1)
    dfs(1, adj, visited)
    
    for i in range(2, n+1):
        print(ans[i])
    
    
if __name__ == '__main__':
    solution()