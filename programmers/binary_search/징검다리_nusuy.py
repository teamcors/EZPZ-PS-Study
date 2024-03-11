def solution(distance, rocks, n):
    answer = 0

    rocks.sort()
    rocks.append(distance)

    left, right = 0, distance
    while left <= right:
        mid = (left + right) // 2
        min_d = distance
        cur = 0
        removed = 0

        for rock in rocks:
            diff = rock - cur
            if diff < mid:
                removed += 1
            else:
                cur = rock
                min_d = min(min_d, diff)

        if removed > n:
            right = mid - 1
        else:
            answer = min_d
            left = mid + 1

    return answer
