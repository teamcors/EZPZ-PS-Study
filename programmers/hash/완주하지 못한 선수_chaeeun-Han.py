def solution(participant, completion):
    answer = ''
    hash = {}
    
    for i in participant:
        hash[i] = hash.get(i, 0) + 1
    
    for k in completion:
        hash[k] -= 1
    for k, v in hash.items():
        if v > 0:
            answer += k
            
    return answer
