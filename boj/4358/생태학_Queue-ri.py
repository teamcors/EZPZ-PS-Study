import sys
from collections import defaultdict

def solution():
    data = defaultdict(int)
    total = 0
    while True:
            type = sys.stdin.readline().rstrip()
            if not type:
                break
            data[type] += 1
            total += 1

        
    datalist = sorted(data.items())
    for k, v in datalist:
        print('{0} {1:.4f}'.format(k, v/total*100))
    
    
if __name__ == '__main__':
    solution()
