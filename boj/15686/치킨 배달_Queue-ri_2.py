import sys
from itertools import combinations
from math import inf
input = sys.stdin.readline

n, m = 0, 0
data = []
home_pos, chicken_pos = [], []
chicken_cand = []

def get_minpath(hpos, cand):
    # cand 하나의 최소 거리 반환
    # hpos : cand = n : 1
    ans = 0
    for h in hpos: # 집 하나 잡아서
        calc_lst = []
        for c in cand: # 폐업처리 완료한 case 하나의 모든 치킨집 좌표 탐색
            calc = abs(h[0]-c[0]) + abs(h[1]-c[1])
            calc_lst.append(calc)
        
        ans += min(calc_lst)
        
    return ans

def solution():
    global n, m, data, home_pos, chicken_pos, chicken_cand
    n, m = map(int, input().split())
    data.append([0] * (n+1)) # padding
    for i in range(1, n+1):
        data.append([0])
        line = list(map(int, input().split()))
        data[i].extend(line)
        for j in range(1, n+1):
            k = line[j-1]
            if k == 1:
                home_pos.append((i, j))
            elif k == 2:
                chicken_pos.append((i, j))
    
    chicken_cand = list(combinations(chicken_pos, m))
    ans = inf
    for cand in chicken_cand:
        ans = min(ans, get_minpath(home_pos, cand))
    
    print(ans)

if __name__ == '__main__':
    solution()