import sys
from collections import defaultdict
from datetime import datetime

def solution():
    end1, start2, end2 = input().split()
    end1 = datetime.strptime(end1, '%H:%M')
    start2 = datetime.strptime(start2, '%H:%M')
    end2 = datetime.strptime(end2, '%H:%M')
    check1 = defaultdict(int)
    check2 = defaultdict(int)
    while True:
        try:
            hr, name = sys.stdin.readline().rstrip().split()
            hr = datetime.strptime(hr, '%H:%M')
            
            if hr <= end1:
                check1[name] += 1
                
            if hr >= start2 and hr <= end2:
                check2[name] += 1
        except:
            break
               
    ans = 0
    for k, v in check1.items():
        if check2[k] > 0:
            ans += 1
            
    print(ans)

    
if __name__ == '__main__':
    solution()
