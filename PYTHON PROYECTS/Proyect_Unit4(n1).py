print ("You are going to create a password to acces the systes, since is your first time you'll have to create a pasword ")

pasword = (input("Here you will put your pasword that must contain 4 digits"))

login = int (3)

while login> 0 :   
    try1 = (input(f"Now you will have {login} attempts to enter your password correctly"))
    if try1 == pasword:
     print ("Your password was entered correctly")
     account = 1
     break
    else:
     login -= 1
     print (f"Your pasword was entered incorrectly you have {login} attempts left")
     account = 0
print ("Welcome" if account ==1 else "Since you have failed at entering your pasword you wil have to create a new account" )
