import sys
input = sys.stdin.readline

ans = 0
abil, member = [], []

def dfs(cnt, sum):
    global ans
    
    if cnt == 11:
        ans = max(ans, sum)
        return
    
    for i in range(11):
        if member[i] or not abil[cnt][i]:
            continue
        
        member[i] = 1
        dfs(cnt+1, sum+abil[cnt][i])
        member[i] = 0
        
    return

def solution():
    global ans, abil, member
    
    c = int(input())
    for __ in range(c):
        abil = [list(map(int, input().split())) for _ in range(11)]
        member = [0] * 11
        ans = 0
        dfs(0, 0)
        print(ans)
    
    
if __name__ == '__main__':
    solution()