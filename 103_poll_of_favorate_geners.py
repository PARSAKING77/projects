from collections import Counter


all = ["Horror", "Romance", "Comedy", "History", "Adventure", "Action"]


n = int(input())


genre_counts = Counter()


for _ in range(n):

    person_data = input().split()
    genres = person_data[1:]
    genre_counts.update(genres)


for genre in all:

    if genre not in genre_counts:
        genre_counts[genre] = 0


sorted_genres = sorted(genre_counts.items(), key=lambda x: (-x[1], x[0]))


for genre, count in sorted_genres:
    print(f"{genre} : {count}")