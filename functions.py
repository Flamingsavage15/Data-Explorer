movies = ['Gladiator', 'Finding Dory', 'Deadpool and Wolverine']
ratings = [8.5, 7, 8.0]
genres = ['Action', 'family', 'action']

print(' ')

def calculate_average_rating(ratings):
    total = sum(ratings)
    return total / len(ratings)
average = calculate_average_rating(ratings)
print('Average Rating:', average)

print(' ')

def find_highest_rated(movies, ratings):
    highest_rating = max(ratings)
    index = ratings.index(highest_rating)
    return movies[index]
top_movie = find_highest_rated(movies, ratings)
print('Top Rated Movie:', top_movie)

print(' ')