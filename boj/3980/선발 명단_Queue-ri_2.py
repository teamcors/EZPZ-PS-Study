import sys
input = sys.stdin.readline

data = []
player = []

def dfs(cur, depth):
    global player
    
    if depth == 11:
        return cur
    
    total = []
    # i: 포지션 번호 / depth: 선수 번호
    for i in range(11):
        if player[i] and data[depth][i]:
            player[i] = 0
            total.append(dfs(cur+data[depth][i], depth+1))
            player[i] = 1
    
    if total:
        return max(total)
    else:
        return -1 # 11번 선수까지 할당 못했을 시 cur값 폐기해야 함

def solution():
    global data
    for _ in range(11):
        data.append(list(map(int, input().split())))
    
    print(dfs(0, 0))
        

if __name__ == '__main__':
    tc = int(input())
    for _ in range(tc):
        data = []
        player = [1] * 11
        solution()