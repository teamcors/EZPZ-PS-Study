from collections import defaultdict

def solution(genres, plays):
    data = []
    
    play_cnt = defaultdict(int)
    for i in range(len(genres)):
        # 장르별 재생횟수 합산
        idx = genres[i]
        play_cnt[idx] += plays[i]
        # 튜플 데이터 생성
        data.append((i, genres[i], plays[i]))
        
    play_cnt = sorted(play_cnt.items(), key=lambda x: x[1], reverse=True)
    genre_order = [i[0] for i in play_cnt]
    data = sorted(data, key=lambda x: (genre_order.index(x[1]), -x[2], x[0]))
    
    answer = []
    prev_genre = ''
    same_cnt = 0
    for i in range(len(data)):
        tup = data[i]
        
        if tup[1] == prev_genre:
            same_cnt += 1
        else:
            same_cnt = 1
            
        prev_genre = tup[1]
        
        if same_cnt > 2:
            continue
        else:
            answer.append(tup[0])
    
    return answer
