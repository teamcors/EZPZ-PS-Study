import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, r, q = 0, 0, 0
adj = []
visited = []
memo = []

def dfs(r):
    global visited
    ans = 1
    
    visited[r] = True
    for x in adj[r]:
        if not visited[x]:
            ans += dfs(x)
    visited[r] = False
    memo[r] = ans
    
    return ans

def solution():
    global n, r, q, adj, visited, memo
    n, r, q = map(int, input().split())
    adj = [[] for _ in range(n+1)]
    visited = [False for _ in range(n+1)]
    memo = [0 for _ in range(n+1)]
    for i in range(n-1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    dfs(r)
    for _ in range(q):
        u = int(input())
        print(memo[u])

if __name__ == '__main__':
    solution()
