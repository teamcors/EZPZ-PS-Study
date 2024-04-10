def solution(money):
    memo1 = [0] * len(money)
    memo2 = [0] * len(money)
    
    # 1번 o
    memo1[0] = money[0]
    for i in range(1, len(money)-1):
        memo1[i] = max(memo1[i-1], memo1[i-2]+money[i])
    
    # 1번 x
    memo1[0] = 0
    for i in range(1, len(money)):
        memo2[i] = max(memo2[i-1], memo2[i-2]+money[i])

    return max(memo1[-2], memo2[-1])