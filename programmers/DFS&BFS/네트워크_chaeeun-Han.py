def dfs(computers, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in range(len(computers[v])):
        if computers[v][i] and not visited[i]:
            dfs(computers, i, visited)
            

def solution(n, computers):
    visited = [False] * n
    answer = 0
    
    for i in range(n):
        if not visited[i]:
            dfs(computers, i, visited)
            answer += 1
    
    return answer
