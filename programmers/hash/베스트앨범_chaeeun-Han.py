def solution(genres, plays):
    answer = []
    genres_dict = {}
    plays_dict = {}

    # genres_dict = genres:[[index, plays], ...]
    # plays_dict = genres:total_plays
    for i in range(len(genres)):
        if genres_dict.get(genres[i], 0) == 0:
            genres_dict[genres[i]] = [[i, plays[i]]]
        else:
            genres_dict[genres[i]].append([i, plays[i]])
        plays_dict[genres[i]] = plays_dict.get(genres[i], 0) + plays[i]

    # 장르 정렬
    plays_dict = dict(
        sorted(plays_dict.items(), key=lambda x: x[1], reverse=True))
    print(plays_dict)

    for v in plays_dict.keys():
        genres_dict[v].sort(key=lambda x: x[1], reverse=True)
        for i in genres_dict[v][:2]:
            answer.append(i[0])
    return answer
