import sys
input = sys.stdin.readline

n, m = 0, 0
data = []
presum = []

def calc(x1, y1, x2, y2):
    return presum[x2][y2] - presum[x2][y1-1] - presum[x1-1][y2] + presum[x1-1][y1-1]

def precalc():
    global presum
    
    for i in range(1, n+1):
        isum = 0
        for j in range(1, m+1):
            isum += data[i][j]
            presum[i][j] = presum[i-1][j] + isum

def solution():
    global n, m, data, presum
    
    n, m = map(int, input().split())
    data = [[0 for _ in range(m+1)]]
    presum = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        data.append([0])
        data[i].extend(list(map(int, input().split())))
        
    precalc()
            
    tc = int(input())
    for _ in range(tc):
        x1, y1, x2, y2 = map(int, input().split())
        print(calc(x1, y1, x2, y2))

if __name__ == '__main__':
    solution()