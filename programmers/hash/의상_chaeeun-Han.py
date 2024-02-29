def solution(clothes):
    answer = 1
    hash = {}

    # 종류별 갯수 파악하기
    for i in clothes:
        hash[i[1]] = hash.get(i[1], 0) + 1

    for v in hash.values():
        answer *= (v+1)

    return answer - 1
