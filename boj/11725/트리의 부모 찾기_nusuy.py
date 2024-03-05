from collections import deque


def solution(n, tree):
    q = deque([0])
    parents = [-1 for _ in range(n)]
    while q:
        c = q.popleft()
        for i in tree[c]:
            if parents[i] == -1:
                parents[i] = c
                q.append(i)
    for i in range(1, n):
        print(parents[i] + 1)


n = int(input())
tree = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    tree[a - 1].append(b - 1)
    tree[b - 1].append(a - 1)

solution(n, tree)
