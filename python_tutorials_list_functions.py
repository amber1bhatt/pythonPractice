##CTRL + SHIFT + B <-- WHEN NO INPUT FROM USER
##OTHERWISE USE BELOW
##Select all CTRL + ENTER
##Or CRTL + ` and run from terminal
##ALT + SHIFT + T for new terminal
##Run from CMD
    ##cd C:\Users\amber\OneDrive\Desktop\Programming\pythonPractice
    ##name_of_file.py

lucky_numbers = [1,2,3,4,5,23, 3, 99, 17, 63, 14, 7]
friends = ["Kevin", "Karen", "Jim", "Bob", "Bob", "Mary", "Martha", "Angus", "Zebra", "Patrick"]

#Extend Function: Take a list and append another list onto it
#friends.extend(lucky_numbers)
#print(friends)

#Append Function: Add an item to the end of a list
friends.append("Marcus")
print(friends)

#Insert Function: Add an item to any place in the list ##Parameters insert(index,item)
friends.insert(1,"Kelly")
print(friends)

#Remove Function: Remove an item from the list
friends.remove("Jim")
print(friends)

#Pop Function: Remove any  element in the list (index)
friends.pop(2)
print(friends)

#Index Function: Find the index value of an element in the list
print(friends.index("Kevin"))

#Count Function: How many times an element appears in the list
print(friends.count("Bob"))

#Sort Function: Sorts the list in alphabetical order and numbers in ascending order
friends.sort()
lucky_numbers.sort()
print(friends)
print(lucky_numbers)

#Reverse Function: Reverse the list
lucky_numbers.reverse()
print(lucky_numbers)

#Copy Function: Take a copy of the list
friends2 = friends.copy()
print(friends2)

#Clear Function: Remove all elements in the list
friends.clear()
print(friends)
