def solution():
    data = input().split()
    
    filter = []
    while True:
        str = input()
        if str == 'what does the fox say?':
            break
        filter.append(str.split()[2])
        
    ans = [e for e in data if e not in filter]

    print(' '.join(ans))


if __name__ == '__main__':
    tc = int(input())
    
    for i in range(tc):
        solution()
