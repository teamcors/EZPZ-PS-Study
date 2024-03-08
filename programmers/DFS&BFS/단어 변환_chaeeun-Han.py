# 28min 09sec
def solution(begin, target, words):
    result = []
    answer = 0
    visited = [False] * len(words)
    
    # 변환할 수 없는 경우
    if target not in words:
        return 0

        
    def dfs(now):
        nonlocal answer

        for word in words:
            dif = cnt = 0
            if not visited[words.index(word)]:
                for i in range(len(word)):
                    if word[i] != now[i]:
                        dif += 1 
                    if now[i] != target[i]:
                        cnt += 1
                        
                if cnt == 1:
                    result.append(answer)
                elif dif == 1:
                    visited[words.index(word)] = True
                    answer += 1
                    dfs(word)
                    
    dfs(begin)
    return min(result) + 1
