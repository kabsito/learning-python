tuples = (1, 2, 3, 4, 5)
print (tuples)
tuple2 = 1,2,3,4,5,55
print (type(tuple2))
print (tuple2)

#tuple2 [0] = 5 This makes an error because tuples are unmutable!

tuple2 = 1,2,3,4,5,55
print (tuple2[3]) #You still can view the number or variable of the tuples in one position

list1 = [1,2,3,4,5]
tuplelist = tuple(list1)
print (type(tuplelist))

l = (1,2,3)
x, y, z = l
print (x, y, z) #You can assing a value of the tuple with x elements to x variables

