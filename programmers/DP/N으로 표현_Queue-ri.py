def solution(N, number):
    memo = [set([int(str(N)*i)]) for i in range(1, 9)]
    
    for i in range(8):
        for j in range(i):
            for n1 in memo[j]:
                for n2 in memo[i-j-1]:
                    memo[i].add(n1 + n2)
                    memo[i].add(n1 - n2)
                    memo[i].add(n1 * n2)
                    if n2:
                        memo[i].add(n1//n2)
        
        if number in memo[i]:
            return i + 1 
    
    return -1