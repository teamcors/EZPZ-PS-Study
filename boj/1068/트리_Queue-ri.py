import sys
input = sys.stdin.readline

children = []

def dfs(cur, target):
    cnt = 0
    if cur == target:
        return 0
    if not children[cur]: # leaf
        return 1
    for nxt in children[cur]:
        cnt += dfs(nxt, target)
    
    if not cnt: # not leaf but none found -> just became leaf
        cnt += 1
    return cnt

def solution():
    global children
    n = int(input())
    data = [int(x) for x in input().rstrip().split(' ')]
    children = [[] for _ in range(n)]
    root = -1
    for i, parent in enumerate(data):
        if ~parent:
            children[parent].append(i)
        else:
            root = i
    target = int(input())
    print(dfs(root, target))

    
if __name__ == '__main__':
    solution()
