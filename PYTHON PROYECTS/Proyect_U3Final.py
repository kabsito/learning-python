score = int(0)

print ("""Today we'll be playing a game made out of four parts.
First we will play a game where you must find the incorrect word between other 3
Second""")

print ("""It will be very easy, I will show you a list of words and you will have to type what is the incorrect word, it will add +1 to a score number you will be able to see at the endo of the hole game""")

question1 = ("tomatoe", "lettuce", "fish", "potatoe")
print (question1)

solution = ("fish")

answer1 = (input("Now write exactly the same word you think is incorrect "))
if answer1 == solution:
    score = (score + 1)
    print ("Your answer was correct, you've earned 1 point with this question")
else:
    print ("Your answer was incorrect, you'll not earn points")

question2 = ("Mercedes", "Mclaren", "Williams", "Cadilac")
print (question2)
solution2 = ("Cadilac")

answer2 = (input("Now write exactly the same word you think is incorrect  "))

if answer2 == solution2:
    score = (score + 1)
    print ("Your answer was correct, you've earned 1 point with this question")
else:
    print ("Your answer was incorrect, you'll not earn points")

question3 = ("scar", "m16", "pump", "barret")
print (question3)
solution3 = ("m16")

answer3 = (input("Now write exactly the same word you think is incorrect "))

if answer3 == solution3:
    score = (score + 1)
    print ("Your answer was correct, you've earned 1 point with this question")
else:
    print ("Your answer was incorrect, you'll not earn points")

print ("Now we'll move to the second game")
print ("Here you have to")