from math import inf

def solution(arr):
    n = len(arr)//2+1
    mn = [[inf for _ in range(n)] for __ in range(n)] # min_memo
    mx = [[-inf for _ in range(n)] for __ in range(n)] # max_memo
    
    for i in range(n):
        mn[i][i] = int(arr[i<<1])
        mx[i][i] = int(arr[i<<1])
    
    for length in range(1, len(mx)):
        for s in range(len(mx)-length):
            e = s + length
            for k in range(s, e):
                if arr[k*2+1] == "+":
                    mx[s][e] = max(mx[s][e],mx[s][k] + mx[k+1][e])
                    mn[s][e] = min(mn[s][e],mn[s][k] + mn[k+1][e])
                elif arr[k*2+1] == '-':
                    mx[s][e] = max(mx[s][e], mx[s][k] - mn[k+1][e])
                    mn[s][e] = min(mn[s][e], mn[s][k] - mx[k+1][e])
    
    return mx[0][-1]