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