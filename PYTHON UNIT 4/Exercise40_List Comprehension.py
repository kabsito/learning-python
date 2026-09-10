squareroot = []
for i in range (5):
    squareroot.append(i**2) #is the same as the next thing but shorter
print (squareroot)

squareroot = [i**2 for i in range (5)]
print (squareroot)

list = [10, 20, 30, 40]

newlist = [i/10 for i in list ]
print (newlist)