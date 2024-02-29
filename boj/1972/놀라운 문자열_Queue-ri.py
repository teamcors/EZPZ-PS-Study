from collections import defaultdict

def solution():
    while True:
        str = input()
        if str == '*':
            break
        
        n = len(str)
        surprising = True
        for d in range(1, n):
            surprising = True
            subdict = defaultdict(int)
            for i in range (n-d):
                subdict[str[i]+str[i+d]] += 1
            
            if any(v > 1 for v in subdict.values()):
                print(str + ' is NOT surprising.')
                surprising = False
                break
            
        if surprising:
            print(str + ' is surprising.')
        
        

if __name__ == '__main__':
    solution()
