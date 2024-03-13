def solution(distance, rocks, n):
    rocks.sort()
    left, right = 0, distance

    while left <= right:
        mid = (left + right) // 2
        remove_cnt = 0
        prev_rock = 0
        
        for rock in rocks:
            if rock - prev_rock < mid:
                remove_cnt += 1
            else:
                prev_rock = rock

        if distance - prev_rock < mid:
            remove_cnt += 1

        if remove_cnt > n:
            right = mid - 1
        else:
            left = mid + 1

    return right
