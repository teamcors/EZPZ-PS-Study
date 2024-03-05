from collections import deque


def check(cw, nw):
    c = 0
    for i, v in enumerate(cw):
        if nw[i] != v:
            c += 1
    return c == 1


def solution(begin, target, words):
    if target not in words:
        return 0

    visited = [0 for _ in range(len(words))]
    steps = dict.fromkeys(words, 0)
    steps[begin] = 1
    q = deque([begin])

    while q:
        c_w = q.popleft()
        for i, v in enumerate(words):
            if visited[i] == 0 and check(c_w, v):
                visited[i] = 1
                steps[v] = steps[c_w] + 1
                q.append(v)

    return steps[target] - 1
