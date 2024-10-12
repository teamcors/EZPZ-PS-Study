import sys
from queue import PriorityQueue
input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    
    idx = m # 추적하려는 문서의 인덱스
    
    pq = PriorityQueue()
    for d in data:
        pq.put(-d)
        
    ans = 0
    while (idx >= 0):
        #print(*data, end=' / ')
        cur = data.pop(0)
        mx = -pq.get()
        #print(idx, cur, mx)

        if cur < mx:
            data.append(cur)
            pq.put(-mx)
            if idx == 0:
                idx = len(data)-1
            else:
                idx -= 1
        else: # print
            ans += 1
            idx -= 1
    
    print(ans)

if __name__ == '__main__':
    tc = int(input())
    
    for _ in range(tc):
        solution()