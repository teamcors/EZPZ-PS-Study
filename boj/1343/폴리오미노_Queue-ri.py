import sys
input = sys.stdin.readline

board = []
n = 0
found = False

def dfs(i):
    global found
    ret = -1
    
    if i >= n:
        if not found:
            print(''.join(board))
            found = True
        return 0
    
    if board[i] == '.':
        ret = dfs(i+1)
        return ret
    
    if i <= n-4:
        if board[i] == 'X' and board[i+1] == 'X' and board[i+2] == 'X' and board[i+3] == 'X':
            board[i] = board[i+1] = board[i+2] = board[i+3] = 'A'
            ret = max(ret, dfs(i+4))
            board[i] = board[i+1] = board[i+2] = board[i+3] = 'X'
    if i <= n-2:
        if board[i] == 'X' and board[i+1] == 'X':
            board[i] = board[i+1] = 'B'
            ret = max(ret, dfs(i+2))
            board[i] = board[i+1] = 'X'
        else:
            return -1
    
    return ret

def solution():
    global board, n
    board = list(input().rstrip())
    n = len(board)
    ret = dfs(0)
    if ret == -1:
        print(-1)

if __name__ == '__main__':
    solution()