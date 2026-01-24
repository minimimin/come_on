from collections import defaultdict

def solution(genres, plays):
    answer = []
    cnt_gen = defaultdict(int)
    gen_songs = defaultdict(list)
    find_gen = []
    
    for idx in range(len(genres)):
        cnt_gen[genres[idx]] += plays[idx]
        gen_songs[genres[idx]].append((-plays[idx], idx))
    for gen in cnt_gen:
        find_gen.append((-cnt_gen[gen],gen))
    find_gen.sort()
    for gen_tu in find_gen:
        gen_songs_list = gen_songs[gen_tu[1]]
        gen_songs_list.sort()
        if len(gen_songs_list) > 1:
            answer.append(gen_songs_list[0][1])
            answer.append(gen_songs_list[1][1])
        elif len(gen_songs_list) == 1:
            answer.append(gen_songs_list[0][1])
    return answer