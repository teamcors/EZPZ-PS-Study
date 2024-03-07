def solution(n, computers):
    def dfs(i):
        v[i] = 1
        for j in range(n):
            if computers[i][j] and not v[j]:
                dfs(j)
                             
    answer = 0
    v = [0 for i in range(len(computers))]
    for i in range(n):
        if not v[i]:
            dfs(i)
            answer += 1
    return answer
