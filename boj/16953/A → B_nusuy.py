from collections import defaultdict


def solution(a, b):
    r = defaultdict(int)
    q = []
    q.append(a)
    r[a] = 0
    while q:
        c = q.pop(0)
        r1 = c * 2
        r2 = c * 10 + 1
        if r1 == b or r2 == b:
            r[b] = r[c] + 1
            q.append(b)
            break
        if r1 < b:
            q.append(r1)
            r[r1] = r[c] + 1
        if r2 < b:
            q.append(r2)
            r[r2] = r[c] + 1
    if not q:
        return -1
    return r[b] + 1
