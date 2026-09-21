print ("Welcome to your shoping list!")

option =int(input('''What would you like to do?
1 - Create a new shopping list
2 - See your last shopping list
3 - exit'''))
while True:
     option =int(input("Press the button that corresponds to the action you want to do "))
     if option in [1,2,3]:
          break
     else:
          continue
