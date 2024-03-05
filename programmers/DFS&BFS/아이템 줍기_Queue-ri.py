from collections import deque

board = []

def draw(rec):
    minX, minY, maxX, maxY = rec
    for k in range(minX, maxX+1):
        board[minY][k] = board[maxY][k] = 1
    for k in range(minY, maxY+1):
        board[k][minX] = board[k][maxX] = 1

def is_outer(y, x, rectangle):
    for rec in rectangle:
        minX, minY, maxX, maxY = rec
        if minY < y and y < maxY and minX < x and x < maxX:
            return False
    
    return True
        
def solution(rectangle, characterX, characterY, itemX, itemY):
    global board
    scale = 2
    
    # scale values
    new_rectangle = []
    for rec in rectangle:
        new_rectangle.append([i * scale for i in rec])
    rectangle = new_rectangle
    
    characterX *= scale
    characterY *= scale
    itemX *= scale
    itemY *= scale
    
    # init
    board = [[0 for _ in range(50 * scale + 2)] for __ in range(50 * scale + 2)]
    for rec in rectangle:
        draw(rec)
    
    # bfs
    q = deque()
    q.append((characterY, characterX, 0))
    board[characterY][characterX] = 0
    
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    
    while q:
        y, x, length = q.popleft()
        if y == itemY and x == itemX:
            return length/2
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if board[ny][nx] and is_outer(ny, nx, rectangle):
                q.append((ny, nx, length+1))
                board[ny][nx] = 0 # visited
        
    return -1 # err
