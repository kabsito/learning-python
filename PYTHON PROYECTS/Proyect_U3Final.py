score = int(0)


print ("""Today we'll be playing a game made out of four parts.
First we will play a game where you must find the incorrect word between other 3
Second""")


print ("""It will be very easy, I will show you a list of words and you will have to type what is the incorrect word, it will add +1 to a score number you will be able to see at the endo of the hole game""")

#-----------------------------------------------------------------------------------
question1 = ["tomatoe", "lettuce", "fish", "potatoe"]
print (question1)


solution = question1.pop(2)


answer1 = (input("Now write exactly the same word you think is incorrect "))
if answer1 == solution:
    score = (score + 1)
    print ("Your answer was correct, you've earned 1 point with this question")
else:
    print ("Your answer was incorrect, you'll not earn points, the correct answer was")
    print (solution)

#------------------------------------------------------------------------------------
question2 = ["Mercedes", "Mclaren", "Williams", "Cadilac"]
print (question2)
solution2 = question2.pop(3)


answer2 = (input("Now write exactly the same word you think is incorrect  "))


if answer2 == solution2:
    score = (score + 1)
    print ("Your answer was correct, you've earned 1 point with this question")
else:
    print ("Your answer was incorrect, you'll not earn points, the correct answer was")
    print (solution2)

#------------------------------------------------------------------------------------
question3 = ["scar", "m16", "pump", "barret"]
print (question3)
solution3 = question3.pop(1)


answer3 = (input("Now write exactly the same word you think is incorrect "))


if answer3 == solution3:
    score = (score + 1)
    print ("Your answer was correct, you've earned 1 point with this question")
else:
    print ("Your answer was incorrect, you'll not earn points, the correct answer was")
    print (solution3)

#-----------------------------------------------------------------------------------
print ("Now we'll move to the second game")
print ("Here you have to tell me the correct number rounded up and the absolute of them")




number1 = 6345.448  
print (F"This is the first number, for the answer just type the number please {number1}")
answernumber1 = int(input("Enter the number here "))


solutionnumber1 = (round(number1))


if solutionnumber1 == answernumber1:
    print ("Your answe was correct you've won 1 point more")
    score = (score + 1)
else:
    print ("Your answer was incorrect, you won't earn points for this question")

numberx = -234.9

absolute = (round(numberx))

solution4 = (abs(absolute))

print (F"This is the second number, for the answer just type the number please {numberx}")
answernumber2 = int(input("Enter the number here "))

if answernumber2 == solution4:
    print ("Your answer was correct")
    score = (score + 1)
else:
    print ("Your answer was incorrect")