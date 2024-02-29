from collections import defaultdict

def solution(clothes):
    cnt = defaultdict(int)
    
    for data in clothes:
        idx = data[1]
        cnt[idx] += 1
        
    val = list(cnt.values())
    
    answer = 1
    for i in val:
        answer *= (i+1)
    
    return answer - 1
