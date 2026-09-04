print ("We will be adding al the numbers of a list you'll create up to five numbers, if you want to stop just put 0")
number1 = int(input("Enter one number ")) #We have to put int to change the type of the variables number 1 to 5 so we are able to sum the up
number2 = int(input("Enter another number "))
number3 = int(input("Enter another number "))
number4 = int(input("Enter another number "))
number5 = int(input("Enter another number "))

number = (number1, number2, number3, number4, number5)
print (f"This is the list of numbers we will add up {number}")

sum1 = sum(number)
print (sum1)
