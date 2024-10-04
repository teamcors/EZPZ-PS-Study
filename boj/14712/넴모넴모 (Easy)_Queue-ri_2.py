import sys
input = sys.stdin.readline

board = []
n, m = 0, 0
dy = [-1, -1, 0]
dx = [0, -1, -1]

def avail(y, x):
    return not (board[y+dy[0]][x+dx[0]] and board[y+dy[1]][x+dx[1]] and board[y+dy[2]][x+dx[2]])
    

def dfs(depth):
    # 네모를 놓고 호출 & 안놓고 호출
    # 4칸 검사 --> 터지면 return 0
    # n, m 도달하면 return 1
    if depth >= n*m:
        return 1
    
    
    cnt = 0
    y = depth // m + 1
    x = depth % m + 1
    
    # 인접 3칸 체크 후 넴모 놓고 다음 탐색
    if avail(y, x): # 놓아도 안터짐
        board[y][x] = True
        cnt += dfs(depth+1)
        board[y][x] = False
    
    # 넴모 안놓고 다음 탐색
    cnt += dfs(depth+1)
    
    
    return cnt

def solution():
    global board, n, m
    n, m = map(int, input().split())
    # depth 계산으로 y, x 구하면 visited 필요 없음
    board = [[False for _ in range(m+1)] for __ in range(n+1)] # 1씩 padding 넣어서 인덱스 검사 생략
    print(dfs(0))
    
if __name__ == '__main__':
    solution()