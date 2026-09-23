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
     print ('''Some things for the creation of your list, it can contain up to 20 elements and in the case" \
     " you want to finish you should put 0 instead''')