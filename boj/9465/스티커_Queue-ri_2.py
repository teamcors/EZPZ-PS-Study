import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = 0
data, memo = [], []

# data를 x축 방향으로 진행하며 매 열마다 선택을 결정하는 방식
def dp(x, status):
    global memo
    
    if x > n-1:
        return 0
    
    if ~memo[x][status]:
        return memo[x][status]
        
    mx = 0
    if status == 0:
        mx += data[0][x] # add left element
        mx += max(dp(x+1,1), dp(x+1,2))
    elif status == 1:
        mx += data[1][x] # add right element
        mx += max(dp(x+1,0), dp(x+1,2))
    else:
        mx += max(dp(x+1,0), dp(x+1,1), dp(x+1,2))
        
    memo[x][status] = mx
    return mx
    
    
def solution():
    global n, data, memo
    n = int(input())
    data.append(list(map(int, input().split())))
    data.append(list(map(int, input().split())))
    memo = [[-1 for _ in range(3)] for _ in range(n)] # 0: left / 1: right / 2: skip
    print(max(dp(0,0), dp(0,1), dp(0,2)))
    

if __name__ == '__main__':
    tc = int(input())
    for _ in range(tc):
        data = []
        solution()