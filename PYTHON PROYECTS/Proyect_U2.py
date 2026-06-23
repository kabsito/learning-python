print ("Hello and welcome to a calculator able to tell you the diferences between numbers and make other opperations.")
n1 = (input)('''The menu of usage of the calculator is very simple just press the following number to make an action:
      1 - multiply all the numbers
      2 - see wich is higher
      3 - see wich one is lower ''')
if n1 =="1":
    n2 = int(input("Now you have to put the numbers you want to multiply: "))
    n3 = int(input("second number: "))
    n4 = int(input("third number: "))
    print (f"The result of the multiplication is ")
    print (n2*n3*n4)
    exit()

elif n1 == "2":
    n2 = int(input("Now you have to put the numbers you want to compare"))
    n3 = int(input("second number"))
    n4 = int(input("third number"))
    print ("The higher number is:")
    if n2>n3>n4 or n2>n4>n3:
        print(n2)
    elif n3>n4>n2 or n3>n2>n4:
        print(n3)
    elif n4>n3>n2 or n4>n2>n3:
        print (n4)
    exit()
elif n1 == "3":
    n2 = int(input("Now you have to put the numbers you want to compare them"))
    n3 = int(input("second number"))
    n4 = int(input("third number"))
    print ("The lower number is:")
    
    if n2<n3<n4 or n2<n4<n3:
        print (n2)
    elif  n3<n4<n2 or n3<n2<n4:
        print (n3)
    elif n4<n3<n2 or n4<n2<n3:
        print (n4) 
    exit()