from collections import deque, defaultdict
from math import inf
from copy import deepcopy

def match(tile, target):
    yt = len(target)
    xt = len(target[0])
    
    if len(tile) == yt and len(tile[0]) == xt:
        cnt = 0
        for i in range(yt):
            for j in range(xt):
                if target[i][j] ^ tile[i][j]:
                    if tile[i][j]: # 타일이 놓아져야 하는 영역인 경우
                        cnt += 1
                else:
                    return False, -999
        return True, cnt
    
    return False, -999

    
def board_bfs(y, x, board):
    board_cp = deepcopy(board)
    q = deque()
    q.append((y, x))
    board_cp[y][x] = 1
    
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    MAX_IDX = len(board)-1
    
    minX, minY, maxX, maxY = inf, inf, -1, -1
    while q:
        i, j = q.popleft()
        
        if i < minY: minY = i
        if maxY < i: maxY = i
        if j < minX: minX = j
        if maxX < j: maxX = j
        
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
        
            if ni < 0 or MAX_IDX < ni or nj < 0 or MAX_IDX < nj:
                continue     
            if not board_cp[ni][nj]:
                q.append((ni, nj))
                board_cp[ni][nj] = 1
            
    slce = []
    for i in range(minY, maxY+1):
        row = board[i]
        slce.append(row[minX:maxX+1])
        
    return slce, board_cp
    

def rotate90(tile):
    y = len(tile)
    x = len(tile[0])
    new_tile = [[] for _ in range(x)]
    for j in range(x):
        for i in range(y-1, -1, -1):
            new_tile[j].append(tile[i][j])
    
    return new_tile


def table_bfs(table, y, x):
    table_cp = deepcopy(table)
    q = deque()
    q.append((y, x))
    table_cp[y][x] = 0 # visited
    
    minX, minY, maxX, maxY = inf, inf, -1, -1
    while q:
        i, j = q.popleft()
        
        if i < minY: minY = i
        if i > maxY: maxY = i
        if j < minX: minX = j
        if j > maxX: maxX = j
        
        di = [-1, 1, 0, 0]
        dj = [0, 0, -1, 1]
        MAX_IDX = len(table)-1
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni < 0 or MAX_IDX < ni or nj < 0 or MAX_IDX < nj:
                continue
            if table_cp[ni][nj]:
                q.append((ni, nj))
                table_cp[ni][nj] = 0 # visited
    
    slce = []
    for i in range(minY, maxY+1):
        row = table[i]
        slce.append(row[minX:maxX+1])
    
    return slce, table_cp


def create_tile_data(table):
    tile_data = defaultdict(list)
    
    idx = 0
    for i in range(len(table)):
        for j in range(len(table[0])):
            if table[i][j]:
                slce, new_table = table_bfs(table, i, j)
                slce90 = rotate90(slce)
                slce180 = rotate90(slce90)
                slce270 =rotate90(slce180)
                tile_data[idx].append(slce)
                tile_data[idx].append(slce90)
                tile_data[idx].append(slce180)
                tile_data[idx].append(slce270)
                table = new_table
                idx += 1
    
    return tile_data


def solution(game_board, table):
    # table에서 tile 영역을 bfs로 찾아 slice해서 dict에 90도 회전한 블록들을 저장
    # list 자체가 해싱이 안돼서 defaultdict(set)은 안되는듯
    tile_data = create_tile_data(table)
    
    MAX_TILE = len(tile_data.keys())
    tile_used = [False for _ in range(MAX_TILE)]
    ans = 0
    # board를 bfs로 탐색해서 0이면 좌상, 우하 좌표 구하기
    for i in range(len(game_board)):
        for j in range(len(game_board[0])):
            if not game_board[i][j]:
                target, board = board_bfs(i, j, game_board)
                game_board = board
    
                # visited가 False인 slice별 회전 목록(dict의 set)을 순회해서
                # 그때의 세로-가로 사이즈가 0공간의 세로-가로와 같은지 체크
                for tidx in range(MAX_TILE):
                    done = False
                    if not tile_used[tidx]:
                        for tile in tile_data[tidx]:
                            # 같으면 영역 반복해서 fill 가능한지 비교하다가 충돌나면 break,
                            # 통과하면 ans += cnt 하고 visited[idx] = True
                            matched, cnt = match(tile, target)
                            if matched:
                                ans += cnt
                                done = True
                                break
                    if done:
                        tile_used[tidx] = True
                        break # goto next target
                                    
    return ans