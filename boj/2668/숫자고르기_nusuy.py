import sys
input = sys.stdin.readline

N = int(input())
num = [0] + [int(input()) for _ in range(N)]

def solution(N, num):
    answer = []

    def dfs(v, i, visited):
        visited[v] = True
        w = num[v]
        if not visited[w]:
            dfs(w, i, visited)
        elif w == i:
            answer.append(w)

    for i in range(1, N + 1):
        visited = [False] * (N + 1)
        dfs(i, i, visited)

    answer.sort()
    s = ""
    l = len(answer)
    for i in range(l):
        s += str(answer[i])
        if i != l - 1:
            s += '\n'
    print(l)
    print(s)

solution(N, num)
