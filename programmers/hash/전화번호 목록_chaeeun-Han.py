def solution(phone_book):
    answer = True
    hash = {}
    
    for i in phone_book:
        hash[i] = 1
        
    for i in phone_book:
        phone = ''
        for j in i:
            phone += j
            if phone in hash and phone != i:
                answer = False
                break
                
    return answer
