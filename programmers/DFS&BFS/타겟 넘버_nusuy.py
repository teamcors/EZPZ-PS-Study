def solution(numbers, target):
    answer = DFS(numbers, target, 0)
    return answer


def DFS(numbers, target, depth):
    answer = 0
    if depth == len(numbers):
        # target과 비교
        if sum(numbers) == target:
            return 1
        else:
            return 0
    else:
        answer += DFS(numbers, target, depth + 1)
        # 현 depth 해당되는 원소값 음수로 변경
        numbers[depth] *= -1
        answer += DFS(numbers, target, depth + 1)
        return answer
