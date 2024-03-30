n = int(input())
cnt = 0
board = [0] * 15

def is_valid(depth):
    for i in range(depth):
        if board[depth] == board[i] or abs(depth - i) == abs(board[depth] - board[i]):
            return False
    return True

def dfs(depth):
    global cnt
    if depth == n:
        cnt += 1
        return

    for i in range(n):
        board[depth] = i
        if (is_valid(depth)):
            dfs(depth + 1)

dfs(0)
print(cnt)
