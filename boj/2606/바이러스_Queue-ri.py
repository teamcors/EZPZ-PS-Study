import sys
from collections import deque, defaultdict
input = sys.stdin.readline

def solution():
    n = int(input())
    m = int(input())
    adj = [[False for _ in range (n+1)] for __ in range(n+1)]
    
    # adj matrix
    for _ in range(m):
        a, b = map(int, input().rsplit())
        adj[a][b] = adj[b][a] = True
    
    # bfs
    visited = [False for _ in range(n+1)]
    q = deque()
    q.append(1)
    visited[1] = True
    ans = 0
    while q:
        k = q.popleft()
        ans += 1
        for i in range(1, n+1):
            if adj[k][i] and not visited[i]:
                q.append(i)
                visited[i] = True

    print(ans-1) # 1번 컴 제외

if __name__ == '__main__':
    solution()