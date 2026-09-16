print ("You are going to create a password to acces the systes, since is your first time you'll have to create a pasword")

pasword = (input("Here you will put your pasword that must contain 4 digits"))

login = int (3)

while login> 0 :   
    try1 = (input(f"Now you will have {login} attempts to enter your password correctly"))
    if try1 == pasword:
     print ("Your password was entered correctly")
     break
    else:
     print ()