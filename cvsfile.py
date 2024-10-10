import csv

with open('action.csv', 'r') as file: 

    reader = csv.reader(file)

def load_movies(filename):
    with open('action.csv', 'r') as file:
        movies = file.readlines()
    return [movie.strip() for movie in movies]

# Write a function -- save_analysis(results, filename) -- that saves analysis results to a file.

def save_analysis(results, bonuscred): 
    with open(bonuscred, 'w') as file: 
        for result in results: 
            file.write(f'{result}\n')
    print(f'Results saved to {bonuscred}')
