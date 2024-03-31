# 53min 35sec
def solution(N, number):
    answer = -1
    dp = []

    # N과 number가 같은 경우 바로 반환
    if N == number:
        return 1

    # i는 N의 갯수
    for i in range(1, 9):
        all_case = set()
        all_case.add(int(str(N)*i))

        for j in range(0, i-1):
            for op1 in dp[j]:
                for op2 in dp[-j-1]:
                    all_case.add(op1 - op2)
                    all_case.add(op1 + op2)
                    all_case.add(op1 * op2)
                    if op2 != 0:
                        all_case.add(int(op1 / op2))

        if number in all_case:
            answer = i
            break

        dp.append(all_case)

    return answer
