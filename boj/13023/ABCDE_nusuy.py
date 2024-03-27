import sys
input = sys.stdin.readline

def dfs(depth, idx, visited):
    global answer
    if depth == 4:
        answer = True
        return

    visited[idx] = True
    for f in friend[idx]:
        if not visited[f]:
            visited[f] = True
            dfs(depth + 1, f, visited)
    visited[idx] = False

def solution(n):
    global answer
    answer = False
    visited = [False] * (n)

    for i in range(n):
        dfs(0, i, visited)
        if answer:
            return 1
    return 0

n, m = map(int, input().split())
friend = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    friend[a].append(b)
    friend[b].append(a)

print(solution(n))
