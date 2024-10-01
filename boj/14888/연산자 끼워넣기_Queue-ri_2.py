import sys
input = sys.stdin.readline

n = 0
nums = []
ops = []

def dfs(res, depth):
    if depth == n:
        return res
    
    mxres = int(-1e9)
    mnres = int(1e9)
    
    if ops[0]:
        ops[0] -= 1
        mn = res[0] + nums[depth]
        mx = res[1] + nums[depth]
        ret = dfs((mn, mx), depth+1)
        mnres = min(ret[0], mnres)
        mxres = max(ret[1], mxres)
        ops[0] += 1
    if ops[1]:
        ops[1] -= 1
        mn = res[0] - nums[depth]
        mx = res[1] - nums[depth]
        ret = dfs((mn, mx), depth+1)
        mnres = min(ret[0], mnres)
        mxres = max(ret[1], mxres)
        ops[1] += 1
    if ops[2]:
        ops[2] -= 1
        mn = res[0] * nums[depth]
        mx = res[1] * nums[depth]
        ret = dfs((mn, mx), depth+1)
        mnres = min(ret[0], mnres)
        mxres = max(ret[1], mxres)
        ops[2] += 1
    if ops[3]:
        ops[3] -= 1
        mn = int(res[0] / nums[depth])
        mx = int(res[1] / nums[depth])
        ret = dfs((mn, mx), depth+1)
        mnres = min(ret[0], mnres)
        mxres = max(ret[1], mxres)
        ops[3] += 1
    
    return (mnres, mxres)

def solution():
    global n, nums, ops
    n = int(input())
    nums = list(map(int, input().split()))
    ops = list(map(int, input().split())) # + - * /
    
    ret = dfs((nums[0],nums[0]), 1)
    print(ret[1])
    print(ret[0])


if __name__ == '__main__':
    solution()