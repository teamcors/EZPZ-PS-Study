import sys
from collections import defaultdict
input = sys.stdin.readline

def solution():
    n, k = map(int, input().split())
    A = map(int, input().split())
    
    ans = 0
    bbhap = 0
    bbhap_dict = defaultdict(int)
    bbhap_dict[0] = 1
    
    for i in A:
        bbhap += i
        
        if bbhap - k in bbhap_dict:
            ans += bbhap_dict[bbhap - k]
            
        bbhap_dict[bbhap] += 1
    
    print(ans)


if __name__ == '__main__':
    solution()