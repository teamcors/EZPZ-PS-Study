# 45min 54sec
import sys
from itertools import combinations
input = sys.stdin.readline

n = int(sys.stdin.readline())
nums = list()   

for i in range(1, 11):      
    for combi in combinations(range(0, 10), i): 
        combi = list(combi)
        combi.sort(reverse=True)                     
        nums.append(int("".join(map(str, combi))))

nums.sort()  

try:
    print(nums[n - 1])
except:
    print(-1)
