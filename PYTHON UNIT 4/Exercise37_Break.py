#Seaching for the first number that can be divided by 7
i = 0
for i in range (1,20):
    if i % 7 == 0:
        print (f"Found the number, it is: {i}")
        break
    print (f"Revising number {i}")

print ("program ended")