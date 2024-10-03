import sys
from collections import defaultdict
input = sys.stdin.readline

data = []
stock = {}


def dfs(res, depth):
    print('res: ' + res + ' depth: ' + str(depth))
    global stock
    
    if depth >= len(data):
        print(res)
        return
    
    # 중복 문자를 key로 뭉쳐놓고 문자 종류별로 하나씩만 고르기 때문에 중복 문자열이 나올 수 없음
    for k in stock:
        if stock[k]:
            stock[k] -= 1
            dfs(res+k, depth+1)
            stock[k] += 1
    
    return 

def solution():
    global data, stock
    data = sorted(list(input().rstrip()))
    stock = defaultdict(int)
    
    for ch in data:
        stock[ch] += 1
        
    dfs('', 0)


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        solution()