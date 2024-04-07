def solution(m, n, puddles):
    answer = 0
    d = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    d[1][1] = 1

    for puddle in puddles:
        d[puddle[1]][puddle[0]] = -1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if d[i][j] == -1:
                d[i][j] = 0
            else:
                d[i][j] += d[i - 1][j] + d[i][j - 1]

    answer = d[n][m] % 1000000007
    return answer
