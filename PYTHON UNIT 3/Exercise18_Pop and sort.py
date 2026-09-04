games = ['Elden ring', 'Jedi survivour', 'RdR II', 'Horizon']
print (games)

last_game = games.pop()
print (last_game)

best_game = games.pop(2)
print (best_game)

movies = ['Shutter Island', 'Godfather', 'Seven', 'Kill Bill']
movies.sort(key=len)#The length of the word
print (movies)
movies.sort()

numbers = [2,56,3,87]
numbers.sort()
print (numbers)
numbers.sort(reverse = True)
print (numbers)