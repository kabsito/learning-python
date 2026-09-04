list1 =[1,2,3,4,]
list1.remove(2)
print (list1)

list2 = {"potatoe", "apple", "tomatoe"}
list2.discard("potatoe")
print (list2)

list3 =["Atlanta", "New York", "Madrid", "Barcelona"]
print ("The removed city is", list3.pop())#The last one is selected
print ("The city in the second place is", list3.pop(1))
list3sub1 = (list3.clear())
print (list3sub1)

s = set([7,4,8,1,9,3,2,6,1])
print (s)