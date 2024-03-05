# 36m 49sec
# 1. bfs: 메모리 초과
# 2. 조건문으로 추가되는 숫자 제어

a, b = map(int, input().split())
cnt = 0
leaves = [a]

while b not in leaves:
    tmp = []
    for parent in leaves:
        n1 = parent * 2
        n2 = int(str(parent)+"1")
        if n1 <= b:
            tmp.append(n1)
        if n2 <= b:
            tmp.append(n2)
    leaves = tmp
    cnt += 1

    if not leaves:
        print(-1)
        break

    for leaf in leaves:
        if leaf == b:
            print(cnt+1)
            break
