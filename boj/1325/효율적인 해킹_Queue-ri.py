import sys
from collections import deque
input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    adj = [[] for _ in range(n+1)]
    
    for i in range(m):
        a, b = map(int, input().split())
        adj[b].append(a)
        
    ans = []
    q = deque()
    for v in range(1, n+1):
        visited = [False for _ in range(n+1)]
        if not visited[v]:
            cnt = 0
            q.append(v)
            visited[v] = True
            while q:
                nv = q.popleft()
                cnt += 1
                for nxt in adj[nv]:
                    if not visited[nxt]:
                        q.append(nxt)
                        visited[nxt] = True
            ans.append((v, cnt))
            
    ans = sorted(ans, key=(lambda x: -x[1]))
    max_val = ans[0][1]
    for x in ans:
        if x[1] == max_val:
            print(x[0], end=' ')


if __name__ == '__main__':
    solution()
