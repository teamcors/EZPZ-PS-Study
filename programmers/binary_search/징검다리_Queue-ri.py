def solution(distance, rocks, n):
    rocks = sorted(rocks)
    
    # midD = min distance between rocks
    minD = 1
    maxD = distance
    
    ans = distance
    while minD <= maxD:
        prev = 0 # start pos
        midD = int((minD + maxD) / 2)
        
        cnt = 0
        for x in rocks:
            if x - prev < midD:
                cnt += 1
            else:
                prev = x
        if distance - prev < midD:
            cnt += 1
        
        if cnt <= n:
            minD = midD + 1
            ans = midD
        else:
            maxD = midD - 1
            
    return ans
