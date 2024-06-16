from collections import defaultdict

def solution(genres, plays):
    answer = []
    songs = defaultdict(list)
    genre_count = defaultdict(int)
    for i in range(len(genres)):
        songs[genres[i]].append((plays[i], i))
        genre_count[genres[i]] += plays[i]
    sorted_genres = sorted(genre_count.items(), key=lambda x: x[1], reverse=True)
    for genre in songs:
        songs[genre] = sorted(songs[genre], key=lambda x: (-x[0], x[1]))
    for max_genre, count in sorted_genres:
        answer.append(songs[max_genre][0][1])
        if len(songs[max_genre]) >= 2:
            answer.append(songs[max_genre][1][1])
    return answer