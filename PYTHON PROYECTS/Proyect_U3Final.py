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
print ("Here you have to tell me the correct number rounded up and the absolute of them")




number1 = 6345.448  
print (F"This is the first number, for the answer just type the number please {number1}")
answernumber1 = (input)


solutionnumber1 = (round(number1))


if solutionnumber1 == answernumber1:
    print ("Your answe was correct you've won 1 point more")
    score = (score + 1)
else:
    print ("Your answer was incorrect, you won't earn points for this question")


number2 = -575.7  
print (F"This is the first number, for the answer just type the number please {number1}")
answernumber2 = (input)


solutionnumber2 = (abs(round(number2)))


if solutionnumber2 == answernumber2:
    print ("Your answe was correct you've won 1 point more")
    score = (score + 1)
else:
    print ("Your answer was incorrect, you won't earn points for this question")




print ("Now for the third and last question you'll have to")



