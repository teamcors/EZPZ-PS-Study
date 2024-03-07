from collections import defaultdict


def solution(nums):
    answer = 0
    mon = defaultdict(int)
    selected = []
    for n in nums:
        mon[n] += 1

    while len(selected) < len(nums) / 2:
        for k in mon.keys():
            if len(selected) == len(nums) / 2:
                break
            if mon[k] > 0:
                if k not in selected:
                    answer += 1
                selected.append(k)
                mon[k] -= 1
    return answer
