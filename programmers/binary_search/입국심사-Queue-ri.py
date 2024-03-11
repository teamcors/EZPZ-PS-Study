from math import inf

def solution(n, times):
    times = sorted(times)
    
    minT = 1
    maxT = times[-1] * n
    ansT = inf
    
    while minT <= maxT:
        midT = int((minT + maxT) / 2)
        # can be done in midT?
        done = 0
        for x in times:
            done += int(midT / x)
        if n <= done:
            ansT = min(ansT, midT)
            maxT = midT - 1
        else:
            minT = midT + 1
    
    return ansT
