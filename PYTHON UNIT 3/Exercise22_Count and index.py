x = [1,1,1,1,1,1,2,2,2,2,3,3,3,4]
print (x.count(1))# First you have to add the variable and a point next to coutn so you are able to select a variable to countthe number of times its in the tuple
print (x.count(2))
print (x.count(3))
print (x.count(4))

y = [1,1,1,1,2,3,3,5,6,6,7,8,8,9]
print (y.index(3))#it works the same but its used to identify in what position is the number you're searching

#Also includes a secon parameter to start looking after a variable when some variables had already passed
print (y.index(3, 6)) 
