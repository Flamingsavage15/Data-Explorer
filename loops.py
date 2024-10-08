movies = ['Gladiator', 'Finding Dory', 'Deadpool and Wolverine']
ratings = [8.5, 7, 8.0]
genres = ['action', 'family', 'action']

for movie in movies: 
    print(movie)

print(' ')

total_rating = 0 
for rating in ratings: 
    total_rating += rating

print('Total Rating:', total_rating)

print(' ')

for r in range(len(movies)):
    print(movies[r], 'has a rating of', ratings[r])

print(' ')

highest_rating = max(ratings)
index = ratings.index(highest_rating)
print('The highest-rated movie is:', movies[index])

print(' ')

filtered_movies = []
for g in range(len(movies)):
    if genres[g] == 'action':
        filtered_movies.append(movies[g])
print('action Movies:', filtered_movies)

print(' ')

