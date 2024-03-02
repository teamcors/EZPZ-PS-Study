lound = int(input())

while lound != 0:
    hash = {}
    answer = 1
    dress = int(input())
    for _ in range(dress):
        a, b = input().split()
        # 없을 시 안 입는 것(default: 1)
        hash[b] = hash.get(b, 1) + 1

    for v in hash.values():
        answer *= v

    print(answer-1)
    lound -= 1
