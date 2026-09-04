print ("You will now have to add five numbers and it will show you the higest and the lowest")
numberlist1 = int(input("number 1: "))
numberlist2 = int(input("number 2: "))
numberlist3 = int(input("number 3: "))
numberlist4 = int(input("number 4: "))
numberlist5 = int(input("number 5: "))

list = [numberlist1, numberlist2, numberlist3, numberlist4, numberlist5]
maxim = (max(list))
minim = (min(list))

print (f"The higher number of this list is {maxim} and the lowest one is {minim}")
