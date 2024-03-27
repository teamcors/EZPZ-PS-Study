# 10min27sec
import sys, itertools as it
input = sys.stdin.readline

n,s = map(int,input().split())
nums = list(map(int,input().split()))
cnt = 0

for i in range(1,n+1):
    for j in list(it.combinations(nums,i)):
        if sum(j)==s:
            cnt+=1
print(cnt)
