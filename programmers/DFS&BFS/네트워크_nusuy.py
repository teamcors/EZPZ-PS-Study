def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]
    for i in range(n):
        if visited[i] == 0:
            answer += 1
            visited[i] = 1
            # 간선 존재 여부 확인
            DFS(n, computers, i, visited)
    return answer


# 이어진 간선 체크
def DFS(n, computers, i, visited):
    for l in range(n):
        # 간선 존재 시
        if computers[i][l] == 1 and visited[l] == 0:
            visited[l] = 1
            DFS(n, computers, l, visited)
