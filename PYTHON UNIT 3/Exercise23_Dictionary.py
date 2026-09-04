my_dictionary = {}
person = {"Name": "Mark", "Age": 34}
print (person)
#Doing the next step we can learn how to extract a specific data of the dictionary
print (person["Name"])

person["Age"] = 10  #we can still make changes on the dictionary
print (person["Age"])

del person["Age"]
print (person["Age"])#Thi will make an error because it no longer exists
