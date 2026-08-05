print ("Welcome to the movie manager, here you will add films to a list and you will be able to create and modify diferent types of films, create ratings and more.")
print ("First you have to enter 5 diferent films please.")

movie1 = input("Now enter the name of the first movie please ")
movie2 = input("Now enter the name of the second movie please ")
movie3 = input("Now enter the name of the third movie please ")
movie4 = input("Now enter the name of the fourth movie please ")
movie5 = input("Now enter the name of the fifth movie please ")

movielist = (movie1, movie2, movie3, movie4, movie5)
print (f"This is your movie list:{movielist}")

n1 = input('''Now you have 3 options to choose between:
 - First, putting 1 in the console will let you add 2 more movies to the list
 - Second
 - Third''')