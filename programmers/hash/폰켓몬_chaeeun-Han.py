def solution(nums):
    hash = {}
    
    for i in nums:
        hash[i] = hash.get(i, 0) + 1
    
    cnt = sum(hash.values())/2
    
    if len(hash.keys()) < cnt:
        return len(hash.keys())
    else:
        return cnt
