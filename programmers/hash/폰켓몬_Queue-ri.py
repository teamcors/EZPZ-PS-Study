def solution(nums):
    answer = 0
    arr = [0] * 200001
    
    for i in nums:
        arr[i] = 1
    
    type_cnt = 0
    n = len(arr)
    k = int(len(nums)/2)

    for i in arr:
        if i == 1:
            type_cnt += 1
    
    answer = k if k < type_cnt else type_cnt
    
    return answer
