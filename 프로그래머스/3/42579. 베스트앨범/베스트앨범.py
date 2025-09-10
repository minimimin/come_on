# 노래 목록_장르구분용 => {장르명 : 총 횟수}
# 노래 목록_개별노래용 => {장르명 : [(-재생횟수, 인덱스), (-재생횟수, 번호)]}
# for 장르 in 장르구분: 길이가 1보다 큰지 확인 => 크면 개별노래[장르].sort() 0번이랑 1번 번호 넣기(2개까지만!!!), 작으면 0만 넣기

from collections import defaultdict

def solution(genres, plays):
    all_songs = len(plays)
    all_genres = defaultdict(int)
    all_plays = defaultdict(list)
    answer = []
    
    # 음악 분류하기
    for i in range(all_songs):
        all_genres[genres[i]] += plays[i]
        all_plays[genres[i]].append((-plays[i], i))
    
    # 가장 많이 재생된 장르 찾기
    all_genre = []
    for name in all_genres:
        all_genre.append((all_genres[name], name))
    all_genre.sort(reverse=True)
    
    # 장르별 2top 뽑기 
    for gen, song_genres in all_genre:
        if len(all_plays[song_genres]) > 1:
            all_plays[song_genres].sort()
            answer.extend((all_plays[song_genres][0][1], all_plays[song_genres][1][1]))
        else:
            answer.append(all_plays[song_genres][0][1])
    return answer