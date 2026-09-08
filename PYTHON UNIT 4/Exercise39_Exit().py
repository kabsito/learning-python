import sys
age = int(input("put a number in the console if its more than 18 it will have an error "))

if age < 18:
    sys.exit("You did correctly the instructions thanks.")
else:
    sys.exit("You did incorectly the instructions.")