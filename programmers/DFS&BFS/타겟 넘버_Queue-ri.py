import sys
from collections import deque
input = sys.stdin.readline

def solution(numbers, target):
    n = len(numbers)
    q = deque()
    q.append(numbers[0])
    q.append(-numbers[0])
    
    for i in range(1, n):
        for _ in range(2**i):
            num = q.popleft()
            q.append(num + numbers[i])
            q.append(num - numbers[i])
    
    ans = 0
    while q:
        if q.popleft() == target:
            ans += 1
    
    return ans