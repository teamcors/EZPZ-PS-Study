from collections import Counter

def solution(participant, completion):
    data = dict(Counter(participant))
    
    for c in completion:
        data[c] -= 1
    
    for p in participant:
        if data[p] > 0:
            return p
    
    return 'err'
