def solution(n, times):
    # 시간의 최소값과 최대값
    left = 1
    right = max(times) * n

    # 이분탐색
    while left <= right:
        mid = (left + right) // 2
        people = 0

        for time in times:
            # 해당 심사대에서 주어진 시간동안 심사 받은 수
            people += mid // time

            # n명 이상 심사 시 중단
            if people >= n:
                break

        # n명 이상 -> 시간이 남았거나, 시간이 너무 많은 경우
        if people >= n:
            answer = mid
            right = mid - 1
        # n명 미만 -> 시간 부족
        else:
            left = mid + 1
    return answer
