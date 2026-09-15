# It allows to write a hole if else in one unique sentence
print ("Now you will try to guess the number I'm thinking, it's a number between 0 and 10 and is a natural number.")

number = int(input ("Enter the umber you think it is the correct "))

result = "Your number was correct!" if number == 4 else "Your number was incorrect, try again!"
print (result)