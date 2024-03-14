from math import inf
import sys

input = sys.stdin.readline

n = int(input())
sour, bitter = [0 for _ in range(n)], [0 for _ in range(n)]
for i in range(n):
    a, b = map(int, input().split())
    sour[i] = a
    bitter[i] = b


def solution(n, sour, bitter):
    def cook(i_sour, i_bitter, v_sour, v_bitter):
        print(i_sour, i_bitter, v_sour, v_bitter)
        global answer
        if i_sour >= n or i_bitter >= n:
            return
        v_sour *= sour[i_sour]
        v_bitter += bitter[i_bitter]

        answer = min(answer, abs(v_sour - v_bitter))
        print(answer)

        cook(i_sour + 1, i_bitter + 1, v_sour, v_bitter)
        cook(
            i_sour + 1,
            i_bitter + 1,
            v_sour // sour[i_sour],
            v_bitter - bitter[i_bitter],
        )

    cook(0, 0, 1, 0)
    return answer


answer = inf
print(solution(n, sour, bitter))
