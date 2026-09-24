print ("Welcome to your shoping list!")

print('''What would you like to do?
1 - Create a new shopping list
2 - See your last shopping list
3 - exit''')
option = int(input("Now enter the number that corresponds to the action you want to make "))
while True:
     if option in [1,2,3]:
          break
     else:
          option =int(input("Press the button that corresponds to the action you want to do "))
          continue

if option == 1:
     print ('''Some things for the creation of your list, it can contain up to 20 elements and in the case \nyou want to finish you should put 0 instead''')

list = []
cant1 = 20
element = 1
while cant1 != 0:
     cant = (cant1 -1)
     item = (input(f"Enter the element number {element} of the list \n"))
     if item == "0":
          cant1= 0
          break
     element = element + 1 
     list.append(item)
     print (f"Your actual shopping list is this {list}")

print ("Now when you have taken a item of your shopping list you can mark it and it will helo you to keep track \nof the items you alrready have!")
print ("You must write the same item and it will apear with a ✔️\n")

variable1 = (input('''Now you can do several things:
'''))
call1 = (input("Enter the name of the item you want to check "))
