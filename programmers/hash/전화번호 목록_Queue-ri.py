def solution(phone_book):
    answer = True
    
    data = sorted(phone_book)
    
    for i in range(len(data)-1):
        cnt = 0
        for j in range(len(data[i])):
            if data[i][j] != data[i+1][j]:
                break
            else:
                cnt += 1
            
        if cnt == len(data[i]):
            return False
    
    return answer
