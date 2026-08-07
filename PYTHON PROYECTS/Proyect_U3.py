print ("Welcome to the movie manager, here you will add films to a list and you will be able to create and modify diferent types of films, create ratings and more.")
print ("First you have to enter 5 diferent films please.")

movie1 = input("Now enter the name of the first movie please ")
movie2 = input("Now enter the name of the second movie please ")
movie3 = input("Now enter the name of the third movie please ")
movie4 = input("Now enter the name of the fourth movie please ")
movie5 = input("Now enter the name of the fifth movie please ")

movielist = [movie1, movie2, movie3, movie4, movie5]
print (f"This is your movie list:{movielist}")

n1 = input('''Now if you wan to add 2 more films put number 1, if not put any other number please.''')
if n1 == "1":
    movie6 = input("Enter you next movie ")
    movie7 = input("Enter your final movie ") 
    movielist = [movie1, movie2, movie3, movie4, movie5, movie6, movie7]

print(f"Your actual movie list is this:{movielist}")

print ("Now for each movie you'll have to put a ranking grade up to 100")

r1 = input(f"For the movie {movie1} enter your grade please ")
r2 = input(f"For the movie {movie2} enter your grade please ")
r3 = input(f"For the movie {movie3} enter your grade please ")
r4 = input(f"For the movie {movie4} enter your grade please ")
r5 = input(f"For the movie {movie5} enter your grade please ")
r6 = input(f"For the movie {movie6} enter your grade please ")
r7 = input(f"For the movie {movie7} enter your grade please ")

dictionarymovies = {f"{movie1}":r1, f"{movie2}":r2, f"{movie3}":r3, f"{movie4}":r4, f"{movie5}":r5, f"{movie6}":r6, f"{movie7}":r7 }
print (f"This  is the complete list of the movies and their grades{dictionarymovies}")
v1 = input ("  ")