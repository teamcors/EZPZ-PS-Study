import sys
from collections import deque
input = sys.stdin.readline

def solution():
    n, target = map(int, input().split())
    q = deque()
    q.append((str(n), 1))
    st = str(target)
    lt = len(st)
    
    while q:
        k, depth = q.popleft()
        if len(k) <= lt:
            q.append((str(int(k)*2), depth+1))
            q.append((k+'1', depth+1))
        if k == st:
            return depth
            
    return -1

if __name__ == '__main__':
    print(solution())
