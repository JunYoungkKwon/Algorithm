from collections import defaultdict

def solution(genres, plays):
    genre_play_sum = defaultdict(int)     # 장르별 총 재생 횟수
    songs = defaultdict(list)             # 장르별 (재생수, 고유번호)

    # 1. 장르별 총 재생 수 및 노래 리스트 저장
    for i in range(len(genres)):
        genre_play_sum[genres[i]] += plays[i]
        songs[genres[i]].append((plays[i], i))


    # 2. 장르 총 재생 횟수로 내림차순 정렬
    sorted_genres = sorted(genre_play_sum.items(), key=lambda x: -x[1])


    answer = []
    key = lambda x: x[0]

    # 3. 각 장르에서 재생수 기준으로 내림차순, 같으면 고유번호 오름차순
    for genre, _ in sorted_genres:
        sorted_songs = sorted(songs[genre], key=lambda x: (-x[0], x[1]))
        # 상위 2개까지 넣기
        for play, idx in sorted_songs[:2]:
            answer.append(idx)

    return answer


# 테스트
genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))   # [3, 0, 4, 1]



