def solution(n, times):
    left, right = 1, min(times) * n
    
    while left <= right:
        mid = (left + right) // 2
        total_people = sum(mid // time for time in times)
        
        if total_people >= n:
            right = mid - 1
        else:
            left = mid + 1

    return left
