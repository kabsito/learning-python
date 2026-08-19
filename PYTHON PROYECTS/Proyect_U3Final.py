score = int(0)

print ("""Today we'll be playing a game made out of four parts.
First we will play a game where you must find the incorrect word between other 3
Second""")

print ("""It will be very easy, I will show you a list of words and you will have to type what is the incorrect word, it will add +1 to a score number you will be able to see at the endo of the hole game""")

question1 = ("tomatoe", "lettuce", "fish", "potatoe")

solution = ("fish")

answer1 = (input("Now write exactly the same wor you think is incorrect "))
if answer1 == answer1:
    score = (score + 1)
    print (score)